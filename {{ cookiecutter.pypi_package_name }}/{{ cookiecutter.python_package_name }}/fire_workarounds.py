"""A collection of workarounds for known issues in our dependencies."""

import colorama
import fire  # type: ignore


def __fire_suppress_pager() -> None:
    """Make Python Fire not use a pager when it prints a help text.

    See also:
    https://github.com/google/python-fire/issues/188#issuecomment-631419585
    """
    fire.core.Display = lambda lines, out: print(*lines, file=out)  # pyright: ignore


def __vscode_code_runner_fix_colors() -> None:
    """Work around an issue in the Code Runner extension for
    Visual Studio Code, which claims to understand ANSI sequences
    but doesn’t actually interpret them.
    """
    colorama.init()


def apply() -> None:
    """Applies all known workarounds."""
    __fire_suppress_pager()
    __vscode_code_runner_fix_colors()
