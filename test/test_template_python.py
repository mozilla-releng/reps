from pprint import pprint

import pytest
from cookiecutter.generate import generate_context
from cookiecutter.prompt import prompt_for_config


def test_generated_files(reps_new):
    name = "foo"
    expected = [
        ".codespell-ignore-words.txt",
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

    project = reps_new(name, "python")

    actual = []
    ignore = ("__pycache__", ".git/", ".pyc", ".venv")
    for path in project.rglob("*"):
        if path.is_dir() or any(i in str(path) for i in ignore):
            continue
        actual.append(str(path.relative_to(project)))

    assert sorted(actual) == sorted(expected)


@pytest.mark.parametrize(
    "extra_context,expected",
    (
        pytest.param(
            {"project_name": "My Package"},
            {
                "__project_slug": "my-package",
                "__package_name": "my_package",
                "short_description": "",
                "author_name": "Mozilla Release Engineering",
                "author_email": "release@mozilla.com",
                "github_slug": "mozilla-releng/my-package",
                "min_python_version": "3.8",
                "__min_tox_python_version": "38",
                "__max_tox_python_version": "312",
                "trust_domain": "mozilla",
                "trust_project": "my-package",
                "level": "1",
                "__codecov_secrets_path": "project/mozilla/my-package/level-any/codecov",  # noqa
                "_copy_without_render": [".github/workflows/codeql-analysis.yml"],
            },
            id="defaults",
        ),
        pytest.param(
            {"project_name": "foo-bar"},
            {"__package_name": "foo_bar"},
            id="package_name_normalized",
        ),
    ),
)
def test_cookiecutter_json(project_root, extra_context, expected):
    cookiecutter_json = (
        project_root / "reps" / "templates" / "python" / "cookiecutter.json"
    )
    context = generate_context(cookiecutter_json, extra_context=extra_context)
    config = prompt_for_config(context, no_input=True)
    pprint(config, indent=2)

    for key, val in expected.items():
        assert key in config
        assert config[key] == val
