import os
import shutil
import subprocess

os.unlink('.venv/.keep')
shutil.rmtree('licenses')

{%- if cookiecutter.use_fire != "y" %}
os.unlink('src/fire_workarounds.py')
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
