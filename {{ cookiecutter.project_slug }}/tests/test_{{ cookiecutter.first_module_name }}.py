# pylint: disable=missing-function-docstring, missing-module-docstring, no-self-use

import {{ cookiecutter.first_module_name }}


def test_hello_with_author_name():
    assert {{ cookiecutter.first_module_name }} \
        .hello('{{ cookiecutter.author_full_name }}') \
        == 'Hello, {{ cookiecutter.author_full_name }}!'


def test_hello_with_no_arguments():
    assert {{ cookiecutter.first_module_name }} \
        .hello() \
        == 'Hello, world!'
