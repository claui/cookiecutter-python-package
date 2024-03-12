# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '{{ cookiecutter.project_title }}'
author = '{{ cookiecutter.author_full_name }} <{{ cookiecutter.author_email }}>'
description = '{{ cookiecutter.project_description }}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

myst_enable_extensions = [
    'deflist',
]

templates_path = []
exclude_patterns = []

# Man page output

man_pages = [(
    'index',
    project.lower(),
    description,
    [author],
    1,
)]
