"""Entry point for the CLI."""

{%- if cookiecutter.use_fire == "y" %}
import fire

{%- endif %}
import {{ cookiecutter.project_slug }}.{{ cookiecutter.first_module_name }} as {{ cookiecutter.first_module_name }}
{%- if cookiecutter.use_fire == "y" %}
import {{ cookiecutter.project_slug }}.fire_workarounds as fire_workarounds

fire_workarounds.apply()
fire.Fire({
    'hello': {{ cookiecutter.first_module_name }}.hello
})
{%- else %}

print({{ cookiecutter.first_module_name }}.hello())
{%- endif %}
