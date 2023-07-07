from pathlib import Path

import pytest

from reps.console import command_new

here = Path(__file__).parent


@pytest.fixture(scope="session")
def datadir():
    return here / "data"


@pytest.fixture(scope="session")
def project_root():
    return here.parent


@pytest.fixture
def reps_new(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp("projects")
    cache = {}

    def inner(name, template="python", **extra_context) -> Path:
        if name in cache:
            return cache[name]

        command_new(
            name,
            template,
            no_input=True,
            extra_context=extra_context,
            output_dir=tmp_path,
        )
        cache[name] = tmp_path / name
        return cache[name]

    return inner
