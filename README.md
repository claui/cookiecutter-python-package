# cookiecutter-python-package

[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for Python projects with a focus on long-term
maintainability and a reliable setup.

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

- project title, slug and version;

- a name for the first module;

- both an author name and a copyright holder name;

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

- a `Pipfile` and an initial lockfile;

- a default linter configuration;

- a pytest script and default configuration;

- `pipenv run` scripts for running the module scripts, tests and the
  linter;

- a virtual environment with initial dependencies installed and
  ready to use;

- a `.gitattributes` file;

- a `.gitignore` file;

- an `.editorconfig` file; and

- settings for Visual Studio Code integration.


## Using cookiecutter-python-package

### Basic usage

To run the template generator, make sure you have a working
Cookiecutter installation. Then run:

```
cookiecutter gh:claui/cookiecutter-python-package
```

### Alternative usage

If you use `cookiecutter-python-package` often, you can add to your
`.cookiecutterrc` an `abbreviations` section like so:

```
abbreviations:
    python: https://github.com/claui/cookiecutter-python-package.git
```

Then, to generate a project, run:

```
cookiecutter python
```


## License

Copyright (c) 2021 Claudia Pellegrino <clau@tiqua.de>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).

### Additional license files

This project may include additional license files other than the
Apache License. Those are just there for the template user’s
convenience so they can choose a license for their own content.
Those licenses may not apply to this project. The only license
that applies to this project is the Apache License.
