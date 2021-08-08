# pylint: disable=missing-function-docstring, missing-module-docstring, no-self-use, too-many-public-methods

import {{ cookiecutter.project_slug }}


def test_hello_with_author_name():
    assert {{ cookiecutter.project_slug }} \
        .hello('{{ cookiecutter.author_full_name }}') \
        == 'Hello, {{ cookiecutter.author_full_name }}!'


def test_hello_with_no_arguments():
    assert {{ cookiecutter.project_slug }}.hello() \
        == 'Hello, world!'
