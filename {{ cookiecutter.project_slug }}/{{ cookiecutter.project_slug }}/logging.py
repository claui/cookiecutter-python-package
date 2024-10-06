"""Customized logging with color support."""

import logging as python_logging

from colorama import Fore, Style

from .settings import debugMode


def get_logger(name: str) -> python_logging.Logger:
    """Instantiate a custom logger with color support."""
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
        python_logging.DEBUG: Style.DIM + _format + Style.RESET_ALL,
        python_logging.INFO: Style.DIM + _format + Style.RESET_ALL,
        python_logging.WARNING: Fore.YELLOW + _format + Style.RESET_ALL,
        python_logging.ERROR: Fore.RED + _format + Style.RESET_ALL,
        python_logging.CRITICAL: Style.BRIGHT
        + Fore.RED
        + _format
        + Style.RESET_ALL,
    }

    def format(self, record: python_logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = python_logging.Formatter(log_fmt)
        return formatter.format(record)
