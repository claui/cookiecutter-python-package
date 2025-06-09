import logging
import os
from pathlib import Path, PurePath
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

{% if cookiecutter.include_executable != "y" -%}
os.remove('.vscode/launch.json')
os.remove('{{ cookiecutter.python_package_name }}/__main__.py')
os.remove('{{ cookiecutter.python_package_name }}/cli.py')
os.remove('{{ cookiecutter.python_package_name }}/fire_workarounds.py')
{% endif -%}

{%- if cookiecutter.install_dependencies_now == "y" %}
try:
    subprocess.run(['uv', 'python', 'install'], check=True, stdout=sys.stderr)
    subprocess.run(['uv', 'lock'], check=True, stdout=sys.stderr)
except subprocess.CalledProcessError as e:
    print(
        f'uv failed with exit code {e.returncode}.',
        'Fix any issues, then go to the '
        '{{ cookiecutter.pypi_package_name }} directory and re-run:',
        f'    {e.cmd}',
        file=sys.stderr,
        sep='\n',
    )
{%- endif %}
