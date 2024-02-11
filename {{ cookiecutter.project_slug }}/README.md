# {{ cookiecutter.project_title }}

## NOTE TO THE PROJECT MAINTAINER

After you’ve done everything in this section, delete the section from
this document.

To allow automatic deployment to TestPyPI, go to the
[Trusted Publisher Management](https://test.pypi.org/manage/account/publishing/)
page and add a new pending publisher with the *Workflow* field set to
`prepare-release.yml`.

To allow automatic deployment to PyPI, go to the
[Trusted Publisher Management](https://test.pypi.org/manage/account/publishing/)
page and add a new pending publisher with the *Workflow* field set to
`pr-post-merge.yml`.

To configure your GitHub repository for the included workflows, go to
your project settings and choose Action » General.

Add the following actions to the *Allow specified actions and reusable
workflows* field:

```plain
EndBug/add-and-commit@v9,
snok/install-poetry@v1,
softprops/action-gh-release@v1,
```

Also make sure that *Workflow permissions* is set to *Read and write
permissions*.

Finally, go to Repository details on the main page of your repository
and enable Releases and Deployments in the *Include in the home page*
section.

Now that you’ve done everything in this section, delete the section from
this document.

## Installation

### Installing from PyPI

To install {{ cookiecutter.project_title }} from PyPI, open a shell and run:

```shell
pip install {{ cookiecutter.project_slug }}
```

If that doesn’t work, try:

```shell
python3 -m pip install {{ cookiecutter.project_slug }}
```

### Installing from the AUR

Direct your favorite
[AUR helper](https://wiki.archlinux.org/title/AUR_helpers) to the
`{{ cookiecutter.package_name }}` package.

## Usage

(tbd)

## Contributing to {{ cookiecutter.project_title }}

See [`CONTRIBUTING.md`](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/blob/main/CONTRIBUTING.md).

## License

{% if cookiecutter.project_license == "Apache-2.0" -%}
{% include 'licenses/Apache-2.0-reference.md' %}
{%- elif cookiecutter.project_license == "Proprietary" -%}
{% include 'licenses/Proprietary-reference.md' %}
{%- endif -%}
