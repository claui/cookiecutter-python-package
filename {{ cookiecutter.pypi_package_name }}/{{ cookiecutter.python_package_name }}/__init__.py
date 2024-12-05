"""
Usage example:

.. code:: python

   from {{ cookiecutter.python_package_name }}.{{ cookiecutter.first_module_name }} import {{ cookiecutter.first_module_name.capitalize() }}

   {{ cookiecutter.first_module_name }} = {{ cookiecutter.first_module_name.capitalize() }}()
   {{ cookiecutter.first_module_name }}.hello()
"""

# Re-export these symbols
# (This promotes them from {{ cookiecutter.python_package_name }}.{{ cookiecutter.first_module_name }} to {{ cookiecutter.python_package_name }})
from {{ cookiecutter.python_package_name }}.{{ cookiecutter.first_module_name }} import {{ cookiecutter.first_module_name.capitalize() }} as {{ cookiecutter.first_module_name.capitalize() }}

from {{ cookiecutter.python_package_name }}.version import version

__all__ = [
    # Modules that every subpackage should see
    'settings',
]

__version__ = version()
