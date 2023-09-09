# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring, no-self-use, too-many-public-methods

from {{ cookiecutter.project_slug }} import hello


def test_hello() -> None:
    assert hello() == 'Hello, world!'


def test_hello_with_author_name() -> None:
    assert hello('{{ cookiecutter.author_full_name }}') \
        == 'Hello, {{ cookiecutter.author_full_name }}!'
