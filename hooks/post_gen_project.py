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
try:
    subprocess.run(
        'pipenv install -d',
        env=pipenv_environment,
        check=True,
        shell=True,
    )
except subprocess.CalledProcessError as e:
    print(
        f'Pipenv failed with exit code {e.returncode}.',
        'Fix any issues, then go to the '
        '{{ cookiecutter.project_slug }} directory and re-run:',
        f'    {e.cmd}',
        sep='\n',
    )
{%- endif %}
