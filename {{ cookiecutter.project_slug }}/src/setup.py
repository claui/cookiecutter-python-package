# pylint: disable=missing-module-docstring

# Usually, when using pipenv to build a stand-alone application,
# no setup.py is required. Still creating one to make pytest happy.
# See also: https://stackoverflow.com/q/50155464

from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages()
)
