import pytest
import yaml


@pytest.fixture(scope="module")
def project_path(copy):
    return copy("sample")


def test_generated_files(project_path):
    name = "sample"
    expected = [
        ".codespell-ignore-words.txt",
        ".copier-answers.yml",
        ".github/CODEOWNERS",
        ".github/workflows/codeql-analysis.yml",
        ".gitignore",
        ".pre-commit-config.yaml",
        ".taskcluster.yml",
        ".yamllint.yml",
        "CODE_OF_CONDUCT.md",
        "LICENSE",
        "Makefile",
        "README.md",
        "docs/concepts/index.rst",
        "docs/conf.py",
        "docs/howto/index.rst",
        "docs/index.rst",
        "docs/reference/index.rst",
        "docs/tutorials/index.rst",
        "pyproject.toml",
        "renovate.json",
        f"src/{name}/__init__.py",
        "taskcluster/config.yml",
        "taskcluster/docker/fetch/Dockerfile",
        "taskcluster/docker/python/Dockerfile",
        "taskcluster/kinds/codecov/kind.yml",
        "taskcluster/kinds/docker-image/kind.yml",
        "taskcluster/kinds/fetch/kind.yml",
        "taskcluster/kinds/test/kind.yml",
        "taskcluster/scripts/codecov-upload.py",
        "test/conftest.py",
        f"test/test_{name}.py",
        "tox.ini",
        "uv.lock",
    ]

    actual = []
    ignore = ("__pycache__", ".git/", ".pyc", ".venv")
    for path in project_path.rglob("*"):
        if path.is_dir() or any(i in str(path) for i in ignore):
            continue
        actual.append(str(path.relative_to(project_path)))

    assert sorted(actual) == sorted(expected)


def test_taskcluster_config_yml(project_path):
    config_path = project_path / "taskcluster" / "config.yml"
    assert config_path.is_file()

    with config_path.open() as fh:
        config = yaml.safe_load(fh)

    assert config["taskgraph"]["cached-task-prefix"] == "mozilla.v2.sample"
