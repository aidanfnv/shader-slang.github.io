---
title: Documentation
layout: docs
description: Documentation
permalink: "/docs/"
---

<div class="container">
    <div id="docs_overview" class="section">
        <div class="row">
            <div class="col-12">
                <h3>Overview
                    <hr>
                </h3>
                {% assign overview_items = site.data.documentation.overview %}
                <div class="grid gridSlang">
                {% for item in overview_items %}
                {% if item.title and item.title != '' %}
                    <div class="g-col-md-4 g-col-sm-6 g-col-12 gridSlang-wrapper">
                        <h4>{{ item.title }}</h4>
                        <p>{{ item.description }}</p>
                        {% if item.link_url and item.link_url != '' %}
                        <p class="gridSlang-link"><a href="{{ item.link_url }}">{{ item.link_label }}</a></p>
                        {% else %}
                        <p class="gridSlang-link">{{ item.link_label }}</p>
                        {% endif %}
                    </div>
                    {% endif %}
                {% endfor %}
                </div>
            </div>
        </div>
    </div>

    <div id="docs_articles" class="section">
        <div class="row">
            <div class="col-12">
                <h3>Articles
                    <hr>
                </h3>
                {% assign articles_items = site.data.documentation.articles %}
                    <div class="grid gridSlang">
                    {% for item in articles_items %}
                    {% if item.title and item.title != '' %}
                        <div class="g-col-md-4 g-col-sm-6 g-col-12 gridSlang-wrapper">
                            <h4>{{ item.title }}</h4>
                            <p>{{ item.description }}</p>
                        {% if item.link_url and item.link_url != '' %}
                        <p class="gridSlang-link"><a href="{{ item.link_url }}">{{ item.link_label }}</a></p>
                        {% else %}
                        <p class="gridSlang-link">{{ item.link_label }}</p>
                        {% endif %}
                        </div>
                    {% endif %}
                    {% endfor %}
                    </div>
            </div>
        </div>
    </div>
    <div id="docs_tutorials" class="section">
        <div class="row">
            <div class="col-12">
                <h3>Tutorials
                    <hr>
                </h3>
                {% assign tutorials_items = site.data.documentation.tutorials %}
                    <div class="grid gridSlang">
                    {% for item in tutorials_items %}
                    {% if item.title and item.title != '' %}
                        <div class="g-col-md-4 g-col-sm-6 g-col-12 gridSlang-wrapper">
                            <h4>{{ item.title }}</h4>
                            <p>{{ item.description }}</p>
                        {% if item.link_url and item.link_url != '' %}
                        <p class="gridSlang-link"><a href="{{ item.link_url }}">{{ item.link_label }}</a></p>
                        {% else %}
                        <p class="gridSlang-link">{{ item.link_label }}</p>
                        {% endif %}
                        </div>
                    {% endif %}
                        {% endfor %}
                    </div>
            </div>
        </div>
    </div>
    
    
    <div class="section">
        <div class="row">
            <div class="col-12">
                <h3>Contributions
                    <hr>
                </h3>
                <p>If you’d like to contribute to the project, we are excited to have your input. Our community pages provides information
                on our structure and our process for accepting contributions.</p>
                <a class="btn btn-primary" href="/community/">Making Community Contributions</a>
            </div>
        </div>
    </div>
</div>

```{toctree}
:caption: Overview
:maxdepth: 1
:titlesonly:

User Guide <https://shader-slang.org/slang/user-guide/>
Standard Modules Reference <external/stdlib-reference/index>
Language Spec <https://github.com/shader-slang/spec>
SlangPy User Guide <https://slangpy.shader-slang.org/en/latest/>
Feature Matureness <feature_matureness>
Command Line Reference <https://github.com/shader-slang/slang/blob/master/docs/command-line-slangc-reference.md>
Frequently Asked Questions <faq>
```

```{toctree}
:caption: Articles
:maxdepth: 1
:titlesonly:

SPIR-V Specific Functionalities <https://shader-slang.org/slang/user-guide/spirv-target-specific.html>
Metal Specific Functionalities <https://shader-slang.org/slang/user-guide/spirv-target-specific.html>
WGSL Specific Functionalities <https://shader-slang.org/slang/user-guide/spirv-target-specific.html>
```

```{toctree}
:caption: Tutorials
:maxdepth: 1
:titlesonly:

Write Your First Slang Shader <first-slang-shader>
Using the Compilation API <compilation-api>
Using the Reflection API <https://shader-slang.org/slang/user-guide/reflection.html>
Shader Cursors: Advanced Usage of the Reflection API <shader-cursors>
Understanding Slang Generics <understanding-generics>
Migrating from HLSL to Slang <coming-from-hlsl>
Using Slang Parameter Blocks <parameter-blocks>
Migrating from GLSL to Slang <coming-from-glsl>
```
