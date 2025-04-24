# SPDX-License-Identifier: Apache-2.0
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))  # Add root directory to path for external references

project = 'Slang Documentation'
author = 'Chris Cummings, Benedikt Bitterli, Sai Bangaru, Yong Hei, Aidan Foster'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

# Configure myst-parser to handle external markdown files
myst_enable_extensions = [
    "colon_fence",
    "linkify",
    "smartquotes",
    "replacements",
    "html_image",
]

# Convert Markdown relative links to HTML properly
myst_url_schemes = ["http", "https", "mailto", "ftp"]
myst_ref_domains = []
myst_update_mathjax = False
myst_heading_anchors = 3
myst_all_links_external = True

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'slang-github': ('https://shader-slang.github.io', None),
}
intersphinx_disabled_domains = ['std']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Add parent directory to the path so external/ can be found
sys.path.insert(0, os.path.abspath('..'))

# Ensure Sphinx includes the submodule
html_extra_path = []

# List of patterns, relative to source directory, that match files and

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = "Slang"
html_static_path = ["_static"]
html_css_files = ["theme_overrides.css"]
html_theme_options = {
    "light_css_variables": {
        "color-api-background": "#f7f7f7",
    },
    "dark_css_variables": {
        "color-api-background": "#1e1e1e",
    },
}

# Add a custom directive to fix relative links
from docutils.parsers.rst.directives.misc import Include
from docutils import nodes
import re

class FixedLinkNode(nodes.reference):
    pass

def visit_fixed_link_html(self, node):
    # Ensure the href doesn't have a leading # if it's a .html file
    href = node.get('refuri', '')
    if href.startswith('#') and '.html' in href:
        node['refuri'] = href[1:]  # Remove the leading #
    self.body.append(self.starttag(node, 'a', '', href=node['refuri']))

def depart_fixed_link_html(self, node):
    self.body.append('</a>')

def setup(app):
    app.add_node(FixedLinkNode,
                 html=(visit_fixed_link_html, depart_fixed_link_html))
    
    # Add a transform to process all links and fix any fragment links that should be relative
    from docutils.transforms import Transform
    
    class FixFragmentLinks(Transform):
        default_priority = 999
        
        def apply(self):
            for node in self.document.traverse(nodes.reference):
                refuri = node.get('refuri', '')
                if refuri.startswith('#') and '.html' in refuri:
                    # This is likely a relative link incorrectly treated as fragment
                    new_node = FixedLinkNode()
                    new_node['refuri'] = refuri[1:]  # Remove the leading #
                    for child in node.children:
                        new_node += child.deepcopy()
                    node.replace_self(new_node)
    
    app.add_transform(FixFragmentLinks)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
