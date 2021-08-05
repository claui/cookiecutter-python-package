"""Root package"""

from {{ cookiecutter.project_slug }}.{{ cookiecutter.first_module_name }} import *

# Make settings module visible for all subpackages
__all__ = ['settings']
