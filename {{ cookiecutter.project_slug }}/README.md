# {{ cookiecutter.project_title }}

## Setting up {{ cookiecutter.project_title }}

To set up {{ cookiecutter.project_title }}, you need three things:

1. The Python version manager `pyenv`.

2. A system-wide Python installation.

3. The Python dependency manager `pipenv`.

### Installing pyenv

The Python version manager `pyenv` makes sure you can always keep
the exact Python version required by {{ cookiecutter.project_title }},
regardless of your system Python.

#### Installing pyenv on Windows

While `pyenv` doesn’t support Windows, you can use a drop-in
replacement called `pyenv-win`.

To install `pyenv-win` on Windows, go to
[github.com/pyenv-win/pyenv-win](https://github.com/pyenv-win/pyenv-win#installation)
and follow one of the installation methods.

#### Installing pyenv on Linux

To install `pyenv` on Linux or WSL2, first make sure Python 3 is
installed. Then follow the _Basic GitHub Checkout_ method described
at [github.com/pyenv/pyenv](https://github.com/pyenv/pyenv#basic-github-checkout).

#### Installing pyenv on macOS

To install `pyenv` on macOS, run:

```
brew install pyenv
```

#### Checking your system-wide pyenv installation

To verify your `pyenv` is working, run:

```
pyenv --version
```

### Checking your system-wide Python installation

Make sure you have Python 3.7 or higher installed on your system
and available in your PATH.

To check, run:

```
python --version
```

If that fails, try:

```
python3 --version
```

Proceed after you’ve confirmed one of those to work.

### Installing pipenv

Install `pipenv` as described under https://pipenv.pypa.io/en/latest/install/#installing-pipenv.

### Finishing up the project setup

- Go to the {{ cookiecutter.project_slug }} directory.

- Run the following command:

```
pipenv install -d
```

## Running {{ cookiecutter.project_title }}

To execute {{ cookiecutter.project_title }}, run:

```
pipenv run cli
```

## Contributing to {{ cookiecutter.project_title }}

### Running the tests

To execute the tests, run:

```
pipenv run tests
```

To execute a single test, run e. g.:

```
pipenv run tests -vv tests/test_{{ cookiecutter.first_module_name }}.py::test_hello
```

### Running the linter

To execute the linter, run:

```
pipenv run linter
```

### Running the static type check

To execute the static type check, run:

```
pipenv run typecheck
```

### Generating project documentation

To generate project documentation and open it in your browser, run:

```
pipenv run doc
```

## Maintenance

### Refreshing dependencies

If you get errors after a Git pull, refresh your dependencies:

```
pipenv install -d
```

### Rebuilding the virtual environment

If you’ve run `pipenv install -d` and you still get errors, rebuild
the virtual environment:

```
pipenv --rm && pipenv install -d
```

### Checking {{ cookiecutter.project_title }}’s dependencies for vulnerabilities

To check {{ cookiecutter.project_title }}’s dependencies for known vulnerabilities, run:

```
pipenv check
```

### Checking {{ cookiecutter.project_title }}’s dependencies for compatible updates

To check {{ cookiecutter.project_title }}’s dependencies for compatible updates, run:

```
pipenv update --dry-run
```

## License

{% if cookiecutter.project_license == "Apache-2.0" -%}
{% include 'licenses/Apache-2.0-reference.md' %}
{%- elif cookiecutter.project_license == "Proprietary" -%}
{% include 'licenses/Proprietary-reference.md' %}
{%- endif -%}
