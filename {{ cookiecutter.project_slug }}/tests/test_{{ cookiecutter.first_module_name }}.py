# pylint: disable=missing-function-docstring, missing-module-docstring, no-self-use, too-many-public-methods

from {{ cookiecutter.project_slug }} import {{ cookiecutter.first_module_name }}


def test_hello() -> None:
    assert {{ cookiecutter.first_module_name }}.hello() \
        == 'Hello, world!'


def test_hello_with_author_name() -> None:
    assert {{ cookiecutter.first_module_name }}.hello('{{ cookiecutter.author_full_name }}') \
        == 'Hello, {{ cookiecutter.author_full_name }}!'
