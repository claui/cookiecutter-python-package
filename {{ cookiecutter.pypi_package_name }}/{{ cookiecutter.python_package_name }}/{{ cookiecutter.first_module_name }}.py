"""The primary module in {{ cookiecutter.python_package_name }}."""

import os
{% if cookiecutter.use_alternative_union_syntax != "y" -%}
from typing import Optional
{% endif %}
{% if cookiecutter.include_executable == "y" -%}
from .errors import CliError
{% endif -%}
from .logging import get_logger

logger = get_logger(__name__)


class {{ cookiecutter.first_module_name.capitalize() }}:  # pylint: disable=too-few-public-methods
    """
    :param foobar:
        The Foobar to connect to.

        Mandatory if no `FOOBAR` environment variable is defined.
        This parameter takes precedence over the environment variable.

    :param qux:
        The path to Qux.

        The default value is: `/path/to/qux`
    """

    def __init__(
        self,
        {% if cookiecutter.use_alternative_union_syntax == "y" -%}
        foobar: str | None = None,
        {%- else -%}
        foobar: Optional[str] = None,
        {%- endif %}
        qux: str = '/path/to/qux',
    ) -> None:
        if (
            merged_foobar := foobar or os.environ.get('FOOBAR', None)
        ) is None:
            {% if cookiecutter.include_executable == "y" -%}
            raise CliError(
                'The `--foobar` switch must be given if '
                + 'no `FOOBAR` environment variable is defined.'
            )
            {%- else -%}
            raise ValueError(
                'The `foobar` argument must be given if '
                + 'no `FOOBAR` environment variable is defined.'
            )
            {%- endif %}
        self._foobar = merged_foobar
        self._qux = qux

    def hello(self, name: str = 'world') -> str:  # pylint: disable=no-self-use
        """Says hello to someone.

        :param name:
            Whom to greet.
            If left empty, we greet the `world`.

        :raises ValueError:
            if `name` is empty.

        :return: a friendly Hello, addressed to `name`.
        """
        if not name:
            raise ValueError('Name cannot be empty.')
        logger.debug('Printing name: %s', name)
        return f'Hello, {name}!'

    def off(self) -> None:  # pylint: disable=no-self-use
        """Disables {{ cookiecutter.project_title }}."""
        logger.info('Disabling {{ cookiecutter.project_title }}')

    def on(self) -> None:  # pylint: disable=no-self-use
        """Enables {{ cookiecutter.project_title }}."""
        logger.info('Enabling {{ cookiecutter.project_title }}')


def hello(
    name: str = 'world',
    {% if cookiecutter.use_alternative_union_syntax == "y" -%}
    foobar: str | None = None,
    {%- else -%}
    foobar: Optional[str] = None,
    {%- endif %}
    qux: str = '/path/to/qux',
) -> str:
    """Says hello to someone.

    :param name:
        Whom to greet.
        If left empty, we greet the `world`.

    :param foobar:
        The Foobar to connect to.

        Mandatory if no `FOOBAR` environment variable is defined.
        This parameter takes precedence over the environment variable.

    :param qux:
        The path to Qux.

        The default value is: `/path/to/qux`

    :raises ValueError:
        if `name` is empty.

    :return: a friendly Hello, addressed to `name`.
    """
    return {{ cookiecutter.first_module_name.capitalize() }}(foobar, qux).hello(name)
