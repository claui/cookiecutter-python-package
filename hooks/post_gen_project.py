import os
import platform
import shutil
import subprocess

shutil.rmtree('licenses')

{%- if cookiecutter.use_fire != "y" %}
os.unlink('{{ cookiecutter.project_slug }}/fire_workarounds.py')
{%- endif %}

{%- if cookiecutter.install_dependencies_now == "y" %}
poetry_environment = os.environ.copy()
poetry_environment.update({
    'LANG': poetry_environment.get('LANG', 'en_US.UTF-8'),
    # https://github.com/python-poetry/poetry/issues/1917
    'PYTHON_KEYRING_BACKEND': 'keyring.backends.null.Keyring',
})

print('Running poetry. This may take a while.')
try:
    subprocess.run(
        'poetry install',
        env=poetry_environment,
        check=True,
        shell=True,
    )
except subprocess.CalledProcessError as e:
    print(
        f'Poetry failed with exit code {e.returncode}.',
        'Fix any issues, then go to the '
        '{{ cookiecutter.project_slug }} directory and re-run:',
        f'    {e.cmd}',
        sep='\n',
    )
{%- endif %}
