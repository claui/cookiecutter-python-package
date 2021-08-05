# pylint: disable=missing-module-docstring

# This is to make the {{ cookiecutter.project_slug }} package
# available in the scope of the project directory.
# See also: https://stackoverflow.com/a/49183765

from setuptools import setup

setup(
    name='project_root',
    packages=['{{ cookiecutter.project_slug }}'],
    include_package_data=True,
)
