# {{ cookiecutter.project_title }}

## Contributing to {{ cookiecutter.project_title }}

See [`CONTRIBUTING.md`](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/blob/main/CONTRIBUTING.md).

## License

{% if cookiecutter.project_license == "Apache-2.0" -%}
{% include 'licenses/Apache-2.0-reference.md' %}
{%- elif cookiecutter.project_license == "Proprietary" -%}
{% include 'licenses/Proprietary-reference.md' %}
{%- endif -%}
