# pylint: disable=missing-function-docstring, missing-module-docstring, no-self-use, too-many-public-methods

import {{ cookiecutter.project_slug }}


def test_hello() -> None:
    assert {{ cookiecutter.project_slug }}.hello() \
        == 'Hello, world!'


def test_hello_with_author_name() -> None:
    assert {{ cookiecutter.project_slug }} \
        .hello('{{ cookiecutter.author_full_name }}') \
        == 'Hello, {{ cookiecutter.author_full_name }}!'
