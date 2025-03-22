# Contributing to cookiecutter-python-package

## Requirements for contributing

To contribute to the `cookiecutter-python-package` template,
you’ll need the project management tool
[uv](https://docs.astral.sh/uv).

### Installing uv

To install uv, see its
[installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

#### Checking your uv installation

To verify uv is working, run:

```shell
uv
```

#### Installing Cookiecutter as a stand-alone tool (optional)

Cookiecutter is already included as a development dependency,
so uv will take care of installing it for you.
You don’t need to have it installed as a stand-alone tool, but you
may still want to do so for your convenience.

To install Cookiecutter as a stand-alone tool, follow Cookiecutter’s [installation
instructions](https://cookiecutter.readthedocs.io/en/stable/installation.html).

## Development scripts and tasks

To see a list of available tasks, run: `uv run poe tasks`

## Running the end-to-end test

To execute the end-to-end test, run: `uv run poe e2e`

## FAQ

Q: Why is Cookiecutter a development dependency even though I
already have a stand-alone Cookiecutter install?

A: This is so your IDE gets to know Cookiecutter’s modules at
development time.
