"""A place for shared paths and settings."""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.absolute()
PACKAGE_ROOT = Path(__file__).parent.absolute()
PYPROJECT_TOML = PROJECT_ROOT / 'pyproject.toml'

PACKAGE_NAME = '{{ cookiecutter.pypi_package_name }}'

debugMode = bool(os.getenv('{{ cookiecutter.python_package_name | upper }}_DEBUG'))
