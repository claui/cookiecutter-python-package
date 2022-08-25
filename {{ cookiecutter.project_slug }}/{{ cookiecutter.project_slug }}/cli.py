"""Entry point for the command line interface."""

import sys

{%- if cookiecutter.use_fire == "y" %}
import fire  # type: ignore
{%- endif %}

from . import {{ cookiecutter.first_module_name }}
{%- if cookiecutter.use_fire == "y" %}
from . import fire_workarounds
{%- endif %}


def run(*args: str) -> None:
    """Runs the command line interface."""
{%- if cookiecutter.use_fire == "y" %}
    fire_workarounds.apply()
    fire.Fire({
        'hello': {{ cookiecutter.first_module_name }}.hello,
    }, command=list(args) + sys.argv[1:]
    )
{%- else %}
    print({{ cookiecutter.first_module_name }}.hello(*args, *sys.argv[1:]))
{%- endif %}
