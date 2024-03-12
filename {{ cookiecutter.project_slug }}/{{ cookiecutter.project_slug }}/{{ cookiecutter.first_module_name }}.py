"""The primary module in {{ cookiecutter.project_slug }}."""

import os
{% if cookiecutter.use_alternative_union_syntax != "y" -%}
from typing import Optional
{% endif %}
from .errors import CliError
from .logging import get_logger

logger = get_logger(__name__)


class {{ cookiecutter.first_module_name.capitalize() }}:
    """
    :param foobar:
        The Foobar to connect to.

        Mandatory if no `FOOBAR` environment variable is defined.
        This parameter takes precedence over the environment variable.

    :param qux:
        The path to Qux.

        The default value is: `/path/to/qux`
    """

    def __init__(self,
        {% if cookiecutter.use_alternative_union_syntax == "y" -%}
        foobar: str | None=None,
        {%- else -%}
        foobar: Optional[str]=None,
        {%- endif %}
        qux: str='/path/to/qux',
    ) -> None:
        if (merged_foobar := foobar or os.environ.get('FOOBAR', None)) is None:
            raise CliError('The `--foobar` switch must be given if ' +
                'no `FOOBAR` environment variable is defined.')
        self._foobar = merged_foobar
        self._qux = qux


    def hello(self, name: str = 'world') -> str:  # pylint: disable=no-self-use
        """Says hello to someone.

        :param `name`:
            whom to greet.
            If left empty, we greet the `world`.

        :raises ValueError:
            if `name` is empty.

        :return: a friendly Hello, addressed to `name`.
        """
        if not name:
            raise ValueError('Name cannot be empty.')
        return f'Hello, {name}!'


    def off(self) -> None:  # pylint: disable=no-self-use
        """Disables {{ cookiecutter.project_title }}."""
        logger.info('Disabling {{ cookiecutter.project_title }}')


    def on(self) -> None:  # pylint: disable=no-self-use
        """Enables {{ cookiecutter.project_title }}."""
        logger.info('Enabling {{ cookiecutter.project_title }}')
