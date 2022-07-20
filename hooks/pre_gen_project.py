import shutil
import sys

MIN_SUPPORTED_PYTHON_VERSION = (3, 7)
if sys.version_info < MIN_SUPPORTED_PYTHON_VERSION:

    _version = ".".join(map(str, MIN_SUPPORTED_PYTHON_VERSION))
    sys.exit(
        f"""
This Cookiecutter template requires Python {_version} or higher.
"""
    )

if '{{ cookiecutter.project_slug }}' \
        == '{{ cookiecutter.first_module_name }}':
    sys.exit('Project slug and first module name cannot be the same')

if not shutil.which('pipenv'):
    sys.exit(
        """
This Cookiecutter template depends on pipenv.
For instructions on how to install pipenv, see:
https://pipenv.pypa.io/en/latest/install/#installing-pipenv
"""
    )
