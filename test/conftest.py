from pathlib import Path

import pytest
import subprocess

here = Path(__file__).parent


@pytest.fixture(scope="session")
def datadir():
    return here / "data"


@pytest.fixture(scope="session")
def project_root():
    return here.parent


@pytest.fixture
def copy(tmp_path_factory, project_root):
    tmp_path = tmp_path_factory.mktemp("projects")
    cache = {}

    def inner(name, template="python", **extra_context) -> Path:
        if name in cache:
            return cache[name]

        extra_context.setdefault("project_name", name)

        project_dir = tmp_path / name
        project_dir.mkdir(exist_ok=True)

        cmd = [
            "copier",
            "copy",
            "--force",
            "--trust",
            "--vcs-ref",
            "HEAD",
            str(project_root),
            "."
        ]

        for key, value in extra_context.items():
            cmd.extend(["-d", f"{key}={value}"])

        result = subprocess.run(cmd, cwd=project_dir, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error applying template {template}:")
            print(result.stderr)

        cache[name] = project_dir
        return cache[name]

    return inner
