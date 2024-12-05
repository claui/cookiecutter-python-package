"""Customized logging{% if cookiecutter.include_executable == "y" %} with color support{% endif %}."""

import logging as python_logging

{% if cookiecutter.include_executable == "y" -%}
from colorama import Fore, Style

{% endif -%}
from .settings import debugMode


def get_logger(name: str) -> python_logging.Logger:
    """Instantiate a custom logger{% if cookiecutter.include_executable == "y" %} with color support{% endif %}."""
    logger = python_logging.getLogger(name)
    logger.setLevel(
        python_logging.DEBUG if debugMode else python_logging.INFO
    )
    handler = python_logging.StreamHandler()
    handler.setFormatter(_CustomFormatter())
    logger.addHandler(handler)
    return logger


class _CustomFormatter(python_logging.Formatter):
    _format = '[%(levelname)s] %(message)s'

    FORMATS = {
        {% if cookiecutter.include_executable == "y" -%}
        python_logging.DEBUG: Style.DIM + _format + Style.RESET_ALL,
        python_logging.INFO: Style.DIM + _format + Style.RESET_ALL,
        python_logging.WARNING: Fore.YELLOW + _format + Style.RESET_ALL,
        python_logging.ERROR: Fore.RED + _format + Style.RESET_ALL,
        python_logging.CRITICAL: Style.BRIGHT
        + Fore.RED
        + _format
        + Style.RESET_ALL,
        {%- else -%}
        python_logging.DEBUG: _format,
        python_logging.INFO: _format,
        python_logging.WARNING: _format,
        python_logging.ERROR: _format,
        python_logging.CRITICAL: _format,
        {%- endif %}
    }

    def format(self, record: python_logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = python_logging.Formatter(log_fmt)
        return formatter.format(record)
