"""Entry point for the command line interface."""

import sys

import fire  # type: ignore

from . import {{ cookiecutter.first_module_name }}, fire_workarounds


def run(*args: str) -> None:
    """Runs the command line interface."""
    fire_workarounds.apply()
    fire.Fire({
        'hello': {{ cookiecutter.first_module_name }}.hello,
    }, command=list(args) + sys.argv[1:]
    )
