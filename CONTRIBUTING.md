# Contributing to cookiecutter-python-package

## Requirements for contributing

To contribute to the `cookiecutter-python-package` template,
you’ll need:

1. The Python version manager `pyenv`.

2. The Python dependency manager `poetry`.

### Installing Poetry

You’ll need `poetry` to manage development dependencies and the venv.

#### Installing Poetry on Windows

To install Poetry on Windows, use one of the
[installation methods](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
described in Poetry’s documentation.

#### Installing Poetry on Linux

If you’re on Linux or WSL2, use your system package manager to
install Poetry.

Alternatively, use one of the
[installation methods](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
described in Poetry’s documentation.

#### Installing Poetry on macOS

To install Poetry on macOS, run:

```shell
brew install poetry
```

#### Checking your Poetry installation

To verify Poetry is working, run:

```shell
poetry --version
```

#### Installing Cookiecutter as a stand-alone tool (optional)

Cookiecutter is already included as a development dependency,
so Poetry will take care of installing it for you.
You don’t need to have it installed as a stand-alone tool, but you
may still want to do so for your convenience.

To install Cookiecutter as a stand-alone tool, follow Cookiecutter’s [installation
instructions](https://cookiecutter.readthedocs.io/en/stable/installation.html).

## Setting up your virtual environment

To set up your virtual environment, follow these steps:

1. Go to the project root directory.

2. Run `pyenv install -s`.

3. Run `pyenv exec python -m venv .venv`.

4. Run `poetry install`.

You need to do the above steps only once.

To update your dependencies after a `git pull`, run `poetry install`.

## Development scripts and tasks

To see a list of available tasks, run: `poetry run poe tasks`

## Running the end-to-end test

To execute the end-to-end test, run: `poetry run poe e2e`

## FAQ

Q: Why is `pyenv` required even though Cookiecutter accepts any
Python version?

A: Especially because Cookiecutter accepts any Python version,
you’ll want your code to work equally well on all of those supported
Pythons. We achieve that by pinning the minimum Python version
that Cookiecutter supports as our development dependency.

Q: Do I have to add `pyenv` shims to my PATH?

A: No, because this guide
[doesn’t use pyenv’s shims](https://github.com/pyenv/pyenv#using-pyenv-without-shims).
It’s still ok to have them in your PATH if you prefer so.

Q: Why is Cookiecutter a development dependency even though I
already have a stand-alone Cookiecutter install?

A: This is so your IDE gets to know Cookiecutter’s modules at
development time.
