# cookiecutter-python-package

[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for Python projects with a focus on long-term
maintainability and a reliable setup.

## About this document

This is the **user documentation** for the Cookiecutter template.  
If you’re a **contributor**, see: [CONTRIBUTING.md](./CONTRIBUTING.md)  
For **license information,** see the bottom of this document.

## About this template

### Goals

`cookiecutter-python-package` is an opinionated Cookiecutter template
for Python projects with a focus on:

- **long-term maintainability** of the generated project (think
  decades, not years);

- **reliability** through step-by-step instructions, enabling users
  to build, run, and work on the generated project on diverse
  platforms;

- using the **latest** Python language and API features; and

- building **runnable programs**, not libraries.

### What you put in

The template allows you to specify:

- project title, slug, description and version;

- a name for the first module;

- both an author name and a copyright holder name;

- the author’s email address;

- a project license (Apache 2.0 or proprietary license);

- a Python major/minor version;

- whether to include the `fire` package, which makes it easier to
  develop a CLI tool;

- whether to include the `jupyter` package; and

- whether to include the `pandas` package.

### What you get out of it

The Cookiecutter template will give you:

- a `README.md` file with detailed instructions;

- a `LICENSE` file;

- the root Python package, located at `{{ cookiecutter.project_slug }}`;

- the first module, located in the root Python package;

- a global settings file that all modules can import;

- a `pyproject.toml` file and an initial Poetry lockfile;

- a default linter configuration;

- a pytest script and default configuration;

- a `pdoc` setup to generate documentation;

- a set of `poe` tasks for running the module scripts, tests and the
  linter (for details, run `poetry run poe tasks`);

- a virtual environment with initial dependencies installed and
  ready to use;

- a `.gitattributes` file;

- a `.gitignore` file;

- an `.editorconfig` file; and

- settings for Visual Studio Code integration.

## Using cookiecutter-python-package

### System requirements

To use this Cookiecutter template, you need:

1. The Python version manager `pyenv`.

2. A system-wide Python installation.

3. Cookiecutter version 2.6.0 or newer.

4. The Python dependency manager `poetry`.

### Installing pyenv

You need the Python version manager `pyenv` so you can set up your
generated package, and to make sure you can always keep that package
up and running, regardless of your system Python.

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

### Installing Cookiecutter

To install Cookiecutter, follow Cookiecutter’s [installation
instructions](https://cookiecutter.readthedocs.io/en/stable/installation.html).

### Installing Poetry

You’ll need `poetry` to manage the generated Python package.

#### Installing Poetry on Windows

To install Poetry on Windows, use one of the
[installation methods](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
described in Poetry’s documentation.

To install Poetry on macOS, run:

```
brew install poetry
```

If you’re on Linux or WSL2, use your system package manager to
install Poetry.

Alternatively, use one of the
[installation methods](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
described in Poetry’s documentation.

#### Checking your Poetry installation

To verify Poetry is working, run:

```
poetry --version
```

### Basic usage

To run the template generator, make sure you have a working
Cookiecutter installation. Then run:

```
cookiecutter gh:claui/cookiecutter-python-package
```

### Alternative usage

If you use `cookiecutter-python-package` often, you can add to your
`.cookiecutterrc` an `abbreviations` section like so:

```yaml
abbreviations:
    python: https://github.com/claui/cookiecutter-python-package.git
```

Then, to generate a project, run:

```shell
cookiecutter python
```

## License

Copyright (c) 2021 – 2024 Claudia Pellegrino <clau@tiqua.de>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).

### Additional license files

This project may include additional license files other than the
Apache License. Those are just there for the template user’s
convenience so they can choose a license for their own content.
Those licenses may not apply to this project. The only license
that applies to this project is the Apache License.
