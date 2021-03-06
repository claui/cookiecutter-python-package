import shutil
import sys

if sys.version_info < (3, 5):
    sys.exit(
        """
This Cookiecutter template requires Python 3.5 or higher.
"""
    )

if not shutil.which('pipenv'):
    sys.exit(
        """
This Cookiecutter template depends on pipenv.
For instructions on how to install pipenv, see:
https://pipenv.pypa.io/en/latest/install/#installing-pipenv
"""
    )
