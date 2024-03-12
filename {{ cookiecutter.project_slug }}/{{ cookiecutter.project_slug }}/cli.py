"""Entry point for the command line interface."""

import sys
from typing import NoReturn

import fire  # type: ignore

from . import {{ cookiecutter.first_module_name }}, fire_workarounds
from .errors import CliError
from .logging import get_logger


logger = get_logger(__name__)


def run(*args: str) -> NoReturn:
    # pylint: disable=magic-value-comparison
    """Runs the command line interface."""
    fire_workarounds.apply()
    try:
        fire.Fire({{ cookiecutter.first_module_name }}.{{ cookiecutter.first_module_name.capitalize() }}, command=list(args) + sys.argv[1:])
    except CliError as e:
        logger.error(e)
        sys.exit(1)
    sys.exit(0)
