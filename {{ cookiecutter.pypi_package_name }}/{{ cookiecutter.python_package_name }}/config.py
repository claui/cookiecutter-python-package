"""User configuration management."""

import json
import os
from typing import Any

import xdg.BaseDirectory  # type: ignore

from .logging import get_logger
from .settings import PACKAGE_NAME

logger = get_logger(__name__)


def config_get(key: str, default: Any | None = None) -> Any | None:
    """Reads a config from the first level of a JSON file by key.

    :param key: the name of the top-level JSON property.

    :param default:
        a default value if the property is not present in the JSON
        or if its value is `null`.
        Defaults to `None`.

    :return:
        the value as a Python object.
        Returns `None` if the JSON value is `null` or if `key` does
        not exist as a property at the top-level.
    """
    path = os.path.join(config_dir(), f'{PACKAGE_NAME}.json')
    if not os.path.exists(path):
        logger.debug(
            'File %s does not exist; interpreting %s == ', path, default
        )
        return default
    with open(path, 'r', encoding='utf-8') as stream:
        config_dict = json.load(stream)
    return config_dict.get(key, default)


def config_set(key: str, value: Any) -> None:
    """Writes a key-value pair to the config JSON file.

    Overwrites an existing property by the given key.

    :param key: the name of the top-level JSON property to store.

    :param value: the value as a Python object, or `None` for `null`.
    """
    path = os.path.join(config_dir(), f'{PACKAGE_NAME}.json')
    if os.path.exists(path):
        with open(path, 'r+', encoding='utf-8') as stream:
            config_dict = json.load(stream) or {}
            if value and value == config_dict.get(key, None):
                logger.debug('Configuration unchanged for key %s', key)
                return
            config_dict[key] = value
            logger.info('Writing new value for key %s: %s', key, value)
            stream.seek(0)
            stream.truncate(0)
            json.dump(config_dict, stream)
            os.fsync(stream)
    else:
        with open(path, 'x', encoding='utf-8') as stream:
            logger.info(
                'Creating configuration file %s with value %s: %s',
                path,
                key,
                value,
            )
            json.dump({key: value}, stream)
            os.fsync(stream)

    logger.info('New value written')


def config_dir(subdir: str | None = None) -> str:
    """Returns the configuration directory for this package.

    Respects the XDG settings. Also creates the directory if it does
    not exist.

    :param subdir: an optional subdirectory, relative to the
                   configuration directory.

    :return: the absolute path to the directory.
    """
    return str(
        xdg.BaseDirectory.save_config_path(
            os.path.join(PACKAGE_NAME, subdir)
            if subdir
            else PACKAGE_NAME
        )
    )
