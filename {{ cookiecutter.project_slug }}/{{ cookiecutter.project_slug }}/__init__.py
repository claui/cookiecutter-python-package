"""
.. include:: ../README.md

## API Documentation
"""

# Re-export these symbols
# (This promotes them from {{ cookiecutter.project_slug }}.{{ cookiecutter.first_module_name }} to {{ cookiecutter.project_slug }})
from {{ cookiecutter.project_slug }}.{{ cookiecutter.first_module_name }} import hello as hello

__all__ = [
    # Tell pdoc to pick up all re-exported symbols
    'hello',

    # Modules that every subpackage should see
    # (This also exposes them to pdoc)
    '{{ cookiecutter.first_module_name }}',
    'settings',
]
