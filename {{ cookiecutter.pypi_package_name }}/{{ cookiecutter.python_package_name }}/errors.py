"""Custom error types."""
{% if cookiecutter.include_executable == "y" %}

class CliError(Exception):
    """A user-facing error message."""
{% endif -%}
