"""
{# See https://wiki.archlinux.org/title/PKGBUILD#license #}
{%
    set spdx_license_dict = {
        "Apache-2.0": "Apache-2.0",
        "Proprietary": "LicenseRef-custom",
    }
%}
{{
    cookiecutter.update({
        "spdx_license":
            spdx_license_dict[cookiecutter.project_license],
        "use_alternative_union_syntax":
            "y" if cookiecutter.python_version.split(".")
                | map("int") | list >= (3, 10) | list
            else "n",
    })
}}
"""

import shutil
import sys

MIN_SUPPORTED_PYTHON_VERSION = (3, 8)
if sys.version_info < MIN_SUPPORTED_PYTHON_VERSION:

    _version = ".".join(map(str, MIN_SUPPORTED_PYTHON_VERSION))
    sys.exit(
        f"""
This Cookiecutter template requires Python {_version} or higher.
"""
    )

if '{{ cookiecutter.python_package_name }}' \
        == '{{ cookiecutter.first_module_name }}':
    sys.exit('Package name and first module name cannot be the same')

if not shutil.which('poetry'):
    sys.exit(
        """
This Cookiecutter template depends on Poetry.
For instructions on how to install Poetry, see `README.md`.
"""
    )
