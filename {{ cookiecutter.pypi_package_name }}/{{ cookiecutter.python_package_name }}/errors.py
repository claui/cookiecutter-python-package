"""Custom error types."""
{% if cookiecutter.include_executable == "y" %}

class CliError(Exception):
    """An user-facing error message."""
{% endif -%}
