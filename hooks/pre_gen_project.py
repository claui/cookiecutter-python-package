import sys

if sys.version_info < (3, 5):
    sys.exit(
        """
This Cookiecutter template requires Python 3.5 or higher.
"""
    )
