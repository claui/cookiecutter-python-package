# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# pylint: skip-file
# type: ignore

project = '{{ cookiecutter.project_title }}'
executable = '{{ cookiecutter.executable_name }}'
author = '{{ cookiecutter.author_full_name }} <{{ cookiecutter.author_email }}>'
description = '{{ cookiecutter.project_description }}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'autoapi.extension',
    'myst_parser',
    'sphinx.ext.autodoc',
]

autoapi_dirs = ['../../{{ cookiecutter.python_package_name }}']
autoapi_keep_files = True
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'special-members',
    'imported-members',
]
autoapi_type = 'python'
autodoc_typehints = 'description'

html_theme = 'sphinx_rtd_theme'

myst_enable_extensions = [
    'deflist',
]


def skip_module(app, what, name, obj, skip, options):
    if what != 'module':
        return skip
    if name in [
        {% if cookiecutter.include_executable == "y" -%}
        '{{ cookiecutter.python_package_name }}.__main__',
        '{{ cookiecutter.python_package_name }}.cli',
        '{{ cookiecutter.python_package_name }}.fire_workarounds',
        {% endif -%}
        '{{ cookiecutter.python_package_name }}.version',
        '{{ cookiecutter.python_package_name }}.settings',
    ]:
        return True
    return skip


def setup(sphinx):
    sphinx.connect('autoapi-skip-member', skip_module)


templates_path = []
exclude_patterns = [
    {% if cookiecutter.include_executable == "y" -%}
    '**/{{ cookiecutter.python_package_name }}/__main__/**',
    '**/{{ cookiecutter.python_package_name }}/cli/**',
    '**/{{ cookiecutter.python_package_name }}/fire_workarounds/**',
    {% endif -%}
    '**/{{ cookiecutter.python_package_name }}/version/**',
    '**/{{ cookiecutter.python_package_name }}/settings/**',
]

# Man page output

man_pages = [
    (
        'usage',
        {% if cookiecutter.include_executable == "y" -%}
        executable,
        {%- else -%}
        '{{ cookiecutter.pypi_package_name }}',
        {%- endif %}
        description,
        [author],
        {% if cookiecutter.include_executable == "y" -%}
        1,
        {%- else -%}
        3,
        {%- endif %}
    )
]

man_show_urls = True
