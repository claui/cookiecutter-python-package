"""Entry point for the command line interface."""

import os
import sys
from typing import NoReturn

import fire  # type: ignore

from . import __version__, {{ cookiecutter.first_module_name }}, fire_workarounds
from .errors import CliError
from .logging import get_logger
from .settings import PROJECT_ROOT, PYPROJECT_TOML


logger = get_logger(__name__)


def _version_text() -> str:
    if __version__ is None:
        return '{{ cookiecutter.project_title }} (unknown version)'
    if os.path.exists(PYPROJECT_TOML):
        return f'{{ cookiecutter.project_title }} v{__version__}' \
            + f' (in development at {PROJECT_ROOT})'
    return f'{{ cookiecutter.project_title }} v{__version__}'


def run(*args: str) -> NoReturn:
    # pylint: disable=magic-value-comparison
    """Runs the command line interface."""

    if sys.argv[1:] and sys.argv[1:][0] in {'-V', '--version'}:
        print(_version_text())
        sys.exit(0)

    fire_workarounds.apply()
    try:
        fire.Fire({{ cookiecutter.first_module_name }}.{{ cookiecutter.first_module_name.capitalize() }}, command=list(args) + sys.argv[1:])
    except CliError as e:
        logger.error(e)
        sys.exit(1)
    sys.exit(0)
