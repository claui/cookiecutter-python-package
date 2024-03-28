"""End-to-end test"""

from tempfile import mkdtemp

from cookiecutter.main import cookiecutter
from .settings import PROJECT_ROOT


def run() -> None:
    """Runs the end-to-end test."""
    target_path_name = cookiecutter(
        str(PROJECT_ROOT),
        no_input=True,
        output_dir=mkdtemp(suffix=".e2e", prefix="cookiecutter."),
        extra_context={
            "project_title": "Flubber",
            "github_username": "end_to_end_test",
            "executable_name": "flub",
            "install_dependencies_now": "n",
        },
    )
    print(target_path_name)
