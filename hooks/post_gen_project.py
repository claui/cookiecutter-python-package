import os
import platform
import shutil
import subprocess

os.unlink('.venv/.keep')
shutil.rmtree('licenses')

# Pick platform-dependent pylint shim
with open('.vscode/settings.json', 'r+') as file:
    content = file.read()
    file.seek(0)
    file.write(content.replace(
        '.SHIM_EXT',
        '.bat' if platform.system() == 'Windows' else '',
    ))
    file.truncate()

{%- if cookiecutter.use_fire != "y" %}
os.unlink('{{ cookiecutter.project_slug }}/fire_workarounds.py')
{%- endif %}

{%- if cookiecutter.install_dependencies_now == "y" %}
pipenv_environment = os.environ.copy()
pipenv_environment.update({
    'LANG': pipenv_environment.get('LANG', 'en_US.UTF-8'),
    'PIPENV_IGNORE_VIRTUALENVS': '1',
    'SYSTEM_VERSION_COMPAT': '1',
})

print('Running pipenv. This may take a while.')
subprocess.run(
    'pipenv install -d',
    env=pipenv_environment,
    check=True,
    shell=True,
)
{%- endif %}
