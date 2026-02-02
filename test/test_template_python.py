def test_generated_files(copy):
    name = "foo"
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

    project = copy(name, "python")

    actual = []
    ignore = ("__pycache__", ".git/", ".pyc", ".venv")
    for path in project.rglob("*"):
        if path.is_dir() or any(i in str(path) for i in ignore):
            continue
        actual.append(str(path.relative_to(project)))

    assert sorted(actual) == sorted(expected)
