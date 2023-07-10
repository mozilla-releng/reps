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
        "poetry.lock",
        f"src/{name}/__init__.py",
        "taskcluster/ci/codecov/kind.yml",
        "taskcluster/ci/config.yml",
        "taskcluster/ci/docker-image/kind.yml",
        "taskcluster/ci/fetch/kind.yml",
        "taskcluster/ci/test/kind.yml",
        "taskcluster/docker/fetch/Dockerfile",
        "taskcluster/docker/python/Dockerfile",
        "taskcluster/requirements.in",
        "taskcluster/requirements.txt",
        "taskcluster/scripts/codecov-upload.py",
        "taskcluster/scripts/pyenv-setup",
        "taskcluster/scripts/poetry-setup",
        "test/conftest.py",
        f"test/test_{name}.py",
        "tox.ini",
    ]

    project = reps_new(name, "python")

    actual = []
    ignore = ("__pycache__", ".git/", ".pyc")
    for path in project.rglob("*"):
        if path.is_dir() or any(i in str(path) for i in ignore):
            continue
        actual.append(str(path.relative_to(project)))

    assert sorted(actual) == sorted(expected)
