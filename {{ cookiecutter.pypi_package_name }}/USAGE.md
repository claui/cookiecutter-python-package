<!-- markdownlint-configure-file { "MD041": { "level": 1 } } -->

# Synopsis

{% if cookiecutter.include_executable == "y" -%}
```shell
{{ cookiecutter.executable_name }} [FLAGS] COMMAND
```
{%- else -%}
*tbd*
{%- endif %}

{% if cookiecutter.include_executable == "y" -%}
# Commands

`COMMAND` is one of the following:

`off`
: Disables {{ cookiecutter.project_title }}.

`on`
: Enables {{ cookiecutter.project_title }}.

# Flags

The following flags are supported:

## `-f`, `--foobar=FOOBAR`

The Foobar to connect to.

Mandatory if no `FOOBAR` environment variable is defined.

The parameter takes precedence over the environment variable.

## `-q`, `--qux=QUX`

The path to Qux.

The default value is: `/path/to/qux`

{% endif -%}
# Environment

{{ cookiecutter.project_title }} supports the following environment variable:

`{{ cookiecutter.python_package_name | upper }}_DEBUG`
: If set to a non-zero value, causes {{ cookiecutter.project_title }} to enable debug-level
: logging.
{% if cookiecutter.include_executable == "y" -%}
: Also prints stack traces for errors where it normally would not.
{% endif -%}
