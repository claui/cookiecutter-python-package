# {{ cookiecutter.project_title }}

## NOTE TO THE PROJECT MAINTAINER

After you’ve done everything in this section, delete the section from
this document.

To allow automatic deployment to TestPyPI, go to the
[Trusted Publisher Management](https://test.pypi.org/manage/account/publishing/)
page and add a new pending publisher with the *Workflow* field set to
`prepare-release.yml` and the *Environment name* set to `testpypi`.

To allow automatic deployment to PyPI, go to the
[Trusted Publisher Management](https://pypi.org/manage/account/publishing/)
page and add a new pending publisher with the *Workflow* field set to
`pr-post-merge.yml` and the *Environment name* set to `pypi`.

To configure your GitHub repository for the included workflows, go to
your project settings and choose Actions » General.

Near the top of the page, choose the option *Allow (your username),
and select non-(your username), actions and reusable workflows*.

Check the two boxes *Allow actions created by GitHub* and *Allow
actions by Marketplace verified creators*.

Then add the following actions to the *Allow specified actions and
reusable workflows* field:

```plain
EndBug/add-and-commit@v9,
snok/install-poetry@v1,
softprops/action-gh-release@v1,
```

Also make sure that *Workflow permissions* is set to *Read and write
permissions* and that the checkbox *Allow GitHub Actions to create
and approve pull requests* is enabled.

Additionally, create an empty commit:

```shell
git commit --allow-empty -m 'Initial commit'
```

Push the commit to your GitHub repository, then refresh the main page
of your repository. Click the small gear icon that appears in the
upper right corner to bring up the Repository settings dialog.
In the *Include in the home page* section, disable Packages but keep
Releases and Deployments enabled.

Now that you’ve done everything in this section, delete the section from
this document.

## Installation

### Installing from PyPI

To install {{ cookiecutter.project_title }} from PyPI, open a shell and run:

```shell
pip install {{ cookiecutter.pypi_package_name }}
```

If that doesn’t work, try:

```shell
python3 -m pip install {{ cookiecutter.pypi_package_name }}
```

### Installing from the AUR

Direct your favorite
[AUR helper](https://wiki.archlinux.org/title/AUR_helpers) to the
`
{%- if cookiecutter.include_executable == "y" -%}
    {{ cookiecutter.pypi_package_name }}
{%- else -%}
    python-{{ cookiecutter.pypi_package_name }}
{%- endif -%}
` package.

## Usage

{% if cookiecutter.include_executable == "y" -%}
```shell
{{ cookiecutter.executable_name }} [FLAGS] COMMAND
```

{% endif -%}
See [`USAGE.md`](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pypi_package_name }}/blob/main/USAGE.md) or `man {{ cookiecutter.executable_name }}` for details.

## Contributing to {{ cookiecutter.project_title }}

See [`CONTRIBUTING.md`](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pypi_package_name }}/blob/main/CONTRIBUTING.md).

## License

{% if cookiecutter.project_license == "Apache-2.0" -%}
{% include 'licenses/Apache-2.0-reference.md' %}
{%- elif cookiecutter.project_license == "Proprietary" -%}
{% include 'licenses/Proprietary-reference.md' %}
{%- endif -%}
