# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring, no-self-use, too-many-public-methods

import pytest

from {{ cookiecutter.project_slug }}.{{ cookiecutter.first_module_name }} import {{ cookiecutter.first_module_name.capitalize() }}


@pytest.fixture(name='{{ cookiecutter.first_module_name }}')
def fixture_{{ cookiecutter.first_module_name }}() -> {{ cookiecutter.first_module_name.capitalize() }}:
    return {{ cookiecutter.first_module_name.capitalize() }}(foobar='baz')


def test_hello({{ cookiecutter.first_module_name }}: {{ cookiecutter.first_module_name.capitalize() }}) -> None:
    assert {{ cookiecutter.first_module_name }}.hello() == 'Hello, world!'


def test_hello_with_author_name({{ cookiecutter.first_module_name }}: {{ cookiecutter.first_module_name.capitalize() }}) -> None:
    assert {{ cookiecutter.first_module_name }}.hello('{{ cookiecutter.author_full_name }}') \
        == 'Hello, {{ cookiecutter.author_full_name }}!'
