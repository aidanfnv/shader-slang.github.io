"""
Custom Sphinx extension to fix relative links with fragment identifiers.
"""
from sphinx.util import logging
import re
import os
from sphinx.application import Sphinx

logger = logging.getLogger(__name__)

def fix_md_links_post_process(app, exception):
    """
    Post-processing to fix links in the HTML output files.
    This is our main function that runs after the build is complete.
    """
    if exception:
        return

    # Only run in HTML builder
    if app.builder.name != 'html':
        return

    output_dir = app.builder.outdir
    logger.info(f"[DEBUG] Post-processing HTML files in {output_dir}")

    # Process all HTML files in the output directory
    count = 0
    fixed = 0

    # Walk through all HTML files
    for root, _, files in os.walk(output_dir):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                count += 1

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Original content for comparison
                    original_content = content

                    # Single pattern to match any href with a path that was incorrectly treated as a fragment
                    # href="#path/to/file.html#anchor" or href="#path/to/file#anchor"
                    pattern = r'href=(["\'])#([^#"\'\s]+)#([^"\'\s]+)\1'
                    
                    matches = re.findall(pattern, content)
                    if matches:
                        logger.info(f"[DEBUG] Found {len(matches)} problematic links in {filepath}")
                        
                        # Fix each match
                        for quote, path, fragment in matches:
                            # Add .html extension if missing and not a directory
                            if not path.endswith('/') and '.' not in path.split('/')[-1]:
                                path_with_html = path + '.html'
                            else:
                                path_with_html = path
                            
                            # Replace in content
                            old = f'href={quote}#{path}#{fragment}{quote}'
                            new = f'href={quote}{path_with_html}#{fragment}{quote}'
                            content = content.replace(old, new)
                            logger.info(f"[DEBUG] Fixed: {old} -> {new}")
                    
                    # Also check for direct references in text (not in href attributes)
                    pattern = r'([a-zA-Z0-9_-]+\.html)#([^#\s]+\.html)#([^#\s"\']+)'
                    matches = re.findall(pattern, content)
                    
                    if matches:
                        logger.info(f"[DEBUG] Found {len(matches)} direct text references in {filepath}")
                        
                        for current_page, target_path, fragment in matches:
                            # Replace in content
                            old = f'{current_page}#{target_path}#{fragment}'
                            new = f'{target_path}#{fragment}'
                            content = content.replace(old, new)
                            logger.info(f"[DEBUG] Fixed direct reference: {old} -> {new}")

                    # Save the file if changes were made
                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixed += 1
                        logger.info(f"[DEBUG] Fixed file: {filepath}")

                except Exception as e:
                    logger.info(f"[DEBUG] Error processing {filepath}: {e}")

    logger.info(f"[DEBUG] Post-processed {count} HTML files, fixed {fixed} files")


def setup(app: Sphinx):
    """Set up the extension."""
    logger.info("[DEBUG] Registering link fixer extension (post-processing only)")

    # Register post-processing function to run after the build is complete
    app.connect('build-finished', fix_md_links_post_process)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }