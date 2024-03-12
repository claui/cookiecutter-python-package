"""
.. include:: ../README.md

## API Documentation
"""

# Re-export these symbols
# (This promotes them from {{ cookiecutter.project_slug }}.{{ cookiecutter.first_module_name }} to {{ cookiecutter.project_slug }})
from {{ cookiecutter.project_slug }}.{{ cookiecutter.first_module_name }} import {{ cookiecutter.first_module_name.capitalize() }} as {{ cookiecutter.first_module_name.capitalize() }}

from {{ cookiecutter.project_slug }}.version import version

__all__ = [
    # Tell pdoc to pick up all re-exported symbols
    '{{ cookiecutter.first_module_name.capitalize() }}',

    # Modules that every subpackage should see
    # (This also exposes them to pdoc)
    '{{ cookiecutter.first_module_name }}',
    'settings',
]

__version__ = version()
