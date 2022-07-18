"""Entry point for the CLI."""

{%- if cookiecutter.use_fire == "y" %}
import fire  # type: ignore
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.first_module_name }}
{%- if cookiecutter.use_fire == "y" %}
from {{ cookiecutter.project_slug }} import fire_workarounds

fire_workarounds.apply()
fire.Fire({
    'hello': {{ cookiecutter.first_module_name }}.hello
})
{%- else %}

print({{ cookiecutter.first_module_name }}.hello())
{%- endif %}
