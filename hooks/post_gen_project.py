import os
import shutil
import subprocess
import sys

shutil.rmtree('licenses')

{%- if cookiecutter.install_dependencies_now == "y" %}
def sysexit_formatted(message: str) -> None:
    width = max((len(line) for line in message))
    print('', width * '-', *message, width * '-',
        file=sys.stderr, sep='\n')
    sys.exit()

pyenv_commands = [
    'pyenv install -s',
    'pyenv exec python -m venv .venv',
]

try:
    for pyenv_command in pyenv_commands:
        subprocess.run(pyenv_command, check=True, shell=True)
except subprocess.CalledProcessError as e:
    sysexit_formatted([
        f'Pyenv failed with exit code {e.returncode}.',
        'Go to the {{ cookiecutter.project_slug }}'
            ' directory and re-run:',
        *[
            f'    {command}'
            for command in pyenv_commands + ['poetry install']
        ],
    ])

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
