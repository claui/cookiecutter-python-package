<!-- markdownlint-configure-file { "MD041": { "level": 1 } } -->

# Synopsis

```shell
{{ cookiecutter.executable_name }} [FLAGS] COMMAND
```

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
