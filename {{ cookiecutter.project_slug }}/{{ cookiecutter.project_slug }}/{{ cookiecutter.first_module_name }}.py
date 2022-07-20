"""This is the description of the {{ cookiecutter.first_module_name }} module."""


def hello(name: str = 'world') -> str:
    """Says hello to someone.

    :param `name`:
        whom to greet.
        If left empty, we greet the `world`.

    :return: a friendly Hello, addressed to `name`.
    """

    return f'Hello, {name}!'
