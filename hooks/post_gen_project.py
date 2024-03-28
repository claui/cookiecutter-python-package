import logging
import os
from pathlib import Path, PurePath
import platform
import shutil
import subprocess
import sys

from cookiecutter.config import get_user_config


logger = logging.getLogger(__name__)

logger.info('Saving replay file for red-port')
config_dict = get_user_config()
template_name = '{{ cookiecutter._repo_dir.split('/')[-1] }}'
target_replay_path = Path('.redport') / 'cookiecutter_replay'
target_replay_path.mkdir(exist_ok=True)
shutil.copy(
    (PurePath(config_dict['replay_dir']) / template_name).with_suffix('.json'),
    target_replay_path,
)

shutil.rmtree('licenses')

{%- if cookiecutter.install_dependencies_now == "y" %}
poetry_environment = os.environ.copy()
poetry_environment.update({
    'LANG': poetry_environment.get('LANG', 'en_US.UTF-8'),
    # https://github.com/python-poetry/poetry/issues/1917
    'PYTHON_KEYRING_BACKEND': 'keyring.backends.null.Keyring',
})

logger.info('Running poetry. This may take a while.')
try:
    subprocess.run(
        'poetry install',
        env=poetry_environment,
        check=True,
        shell=True,
        stdout=sys.stderr,
    )
except subprocess.CalledProcessError as e:
    print(
        f'Poetry failed with exit code {e.returncode}.',
        'Fix any issues, then go to the '
        '{{ cookiecutter.project_slug }} directory and re-run:',
        f'    {e.cmd}',
        file=sys.stderr,
        sep='\n',
    )
{%- endif %}
