"""Entry point for the command line interface."""

from collections.abc import Generator
from contextlib import contextmanager
import os
import sys
from typing import NoReturn

import fire  # type: ignore

from . import __version__, {{ cookiecutter.first_module_name }}, fire_workarounds
from .errors import CliError
from .logging import get_logger
from .settings import PROJECT_ROOT, PYPROJECT_TOML


logger = get_logger(__name__)


def run(*args: str) -> None:
    """Runs the command line interface."""
    with _cli_context(*args) as combined_args:
        fire.Fire({{ cookiecutter.first_module_name }}.{{ cookiecutter.first_module_name.capitalize() }}, command=combined_args)


def hello(*args: str) -> None:
    """Runs the `hello` CLI subcommand directly."""
    with _cli_context(*args) as combined_args:
        fire.Fire({{ cookiecutter.first_module_name }}.hello, command=combined_args)


@contextmanager
def _cli_context(*args: str) -> Generator[list[str], None, NoReturn]:
    combined_args = list(args) + sys.argv[1:]
    if combined_args and combined_args[0] in {'-V', '--version'}:
        print(_version_text())
        sys.exit(0)

    fire_workarounds.apply()
    try:
        yield combined_args
    except CliError as e:
        logger.error(e)
        sys.exit(1)
    sys.exit(0)


def _version_text() -> str:
    if __version__ is None:
        return '{{ cookiecutter.project_title }} (unknown version)'
    if os.path.exists(PYPROJECT_TOML):
        return (
            f'{{ cookiecutter.project_title }} v{__version__}'
            + f' (in development at {PROJECT_ROOT})'
        )
    return f'{{ cookiecutter.project_title }} v{__version__}'
