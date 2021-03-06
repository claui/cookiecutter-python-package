import os
import shutil
import subprocess

os.unlink('.venv/.keep')
shutil.rmtree('licenses')

subprocess.run(
    'pipenv install -d',
    env={
        'LANG': 'en_US.UTF-8',
        'PIPENV_IGNORE_VIRTUALENVS': '1',
        'SYSTEM_VERSION_COMPAT': '1',
    },
    check=True,
    shell=True,
)
