# Release Engineering Project Standard

## Motivation

The Release Engineering Project Standard (REPS) aims to provide a consistent
set of tools and workflows that can be used across all of Release Engineering’s
projects.

Using consistent tooling across projects unlocks many benefits by allowing us
to be proficient with a single set of tools rather than needing to learn new
ones for each project. This increases productivity, makes onboarding easier and
enables seamless context switching between projects. Consistent tooling also
helps set the bar for code standards and quality, ensuring all projects meet
the same baseline.

## General

All projects should follow these general standards.

### Version Control

Projects should use Git and be hosted on Github. In most cases, new projects
should be created in the mozilla-releng org, but may live in other Mozilla
affiliated orgs when appropriate.

#### Branch Protection

Projects should enable branch protection for the main branch and any other
branches where releases are created.

At a minimum, the following protections should be enabled:

* Require a pull request before merging
* Require approvals (1)
* Require review from Code Owners
* Require status checks to pass before merging (which checks are discretionary)

Additionally, the following rules should not be checked:

* Allow force pushes
* Allow deletions

#### Hooks

Projects should provide commit and push hooks that can run relevant linters and
formatters. The [pre-commit] tool should be used to provide these hooks.

The following should be added to `.pre-commit-config.yaml` at the project root:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    - id: trailing-whitespace
    - id: end-of-file-fixer
    - id: check-yaml
    - id: check-added-large-files
  - repo: https://github.com/codespell-project/codespell
    rev: v2.2.4
    hooks:
    - id: codespell
        entry: codespell -I .codespell-ignore-words.txt
```

Run `pre-commit autoupdate` to update tools to their latest versions.

Additionally, language specific linters and formatters should be added (see
sections below).

[pre-commit]: https://pre-commit.com/

### CI / CD

#### Taskcluster

Nearly all continuous integration should be run on the [Firefox-CI Taskcluster
instance] and use [Taskgraph], with a few exceptions outlined below.

In general, projects should at a minimum have a test task that invokes the
tests and generates test coverage reports and a CodeCov upload task that
uploads reports to CodeCov.io.

##### pullRequest policy

Projects should use the `public_restricted` pull request policy. This is
mandatory if it requires any secrets that are used in pull requests (for
example, the token for CodeCov.io). This can be done by adding the following to
the root `.taskcluster.yml`:

```yaml
policy:
    pullRequests: public_restricted
```

##### autoCancelPreviousChecks

Projects should enable Taskcluster's `autoCancelPreviousChecks` feature to save
cost when pushing new changes to a pull request by adding the following to their
root `.taskcluster.yml`:

```yaml
autoCancelPreviousChecks: true
```

[Firefox-CI Taskcluster instance]: https://firefox-ci-tc.services.mozilla.com/
[Taskgraph]: https://github.com/taskcluster/taskgraph

#### Github Actions

##### Pre-commit Action

Releng hosts shared Github actions under `mozilla-releng/actions`. The
`pre-commit` action can be used instead of Taskcluster as it's simpler to
share.

##### CodeQL Action

Github offers free vulnerability scanning for public repos via [CodeQL].

The [default setup] should be enabled and run via Github Actions.

[CodeQL]: https://codeql.github.com/
[default setup]: https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning-for-a-repository#configuring-code-scanning-automatically

#### CodeCov.io

[Codecov.io] should be used to ensure test coverage is trending in the right
direction.

The [codecov.io Github integration] should be enabled, the default configuration
(no config file) is sufficient. These checks should not be “required” (e.g
block PRs from landing), but used as a nudge to improve test coverage.

[CodeCov.io]: http://codecov.io
[codecov.io Github integration]: https://github.com/apps/codecov

#### Renovate

We use [RenovateBot] to keep dependencies up to date. This repository contains a [Shareable Config Preset] for that service, and a default configuration that points projects bootstrapped from this repository at it. You should avoid custom config in other repositories if at all possible, and prefer to upstream any changes to the config hosted here.

[RenovateBot]: https://docs.renovatebot.com/
[Shareable Config Preset]: https://docs.renovatebot.com/config-presets/#shareable-config-presets

### Documentation

Documentation should be generated using [Sphinx], written with reStructuredText
and live under a top-level `docs` directory. Documentation should be built and
hosted on [readthedocs.org]. A `.readthedocs.yaml` file should be included at the
root of the project that looks similar to:

```yaml
---
version: 2
build:
    os: ubuntu-20.04
    tools:
        python: "3.9"
python:
    install:
        - requirements: requirements/docs.txt
        - method: pip
        path: .
sphinx:
    configuration: docs/conf.py
```

[Sphinx]: https://www.sphinx-doc.org/en/master/
[readthedocs.org]: https://readthedocs.org/

#### Content Structure

As much as reasonably possible, documentation should try to follow the [Diátaxis
technical documentation framework]. That is, try to break documentation down
into the following four broad categories:

* Learning oriented (tutorials)
* Task oriented (how-to guides)
* Understanding oriented (explanations)
* Information oriented (references)

Not all projects will need docs for each category, nor will docs always break
down nicely into these categories. The framework is simply something to keep in
mind and strive towards on a best effort basis.

[Diátaxis technical documentation framework]: https://diataxis.fr/

### Code Coverage

Projects should track and report code coverage using CodeCov.io. While higher
code coverage is better, projects should not enforce or have explicit goals to
reach 100% coverage.

Instead, projects should aim to incrementally improve coverage via nudges
through failing CI tasks when coverage has decreased. These CI failures should
not be marked as `Required` in the branch protection rules, so they can easily be
bypassed if needed.

The default configuration from CodeCov is sufficient to meet these
requirements.

[CodeCov.io]: https://about.codecov.io/

### Linting

Projects should run the following linters regardless of language they use:

* [yamllint] to catch issues in task configuration or dot-files
* [rstcheck] to catch issues in documentation
* [codespell] to catch spelling mistakes in comments

Yamllint should be configured in a top-level `.yamllint.yml` file:

```yaml
---
extends: default

rules:
    document-end:
        present: false
    line-length: disable

ignore: |
  .tox
```

Rstcheck should be installed with the `sphinx` and `toml` extras. The default
configuration is sufficient. Should additional configuration be required, it
should go in the `tool.rstcheck` section of the top-level `pyproject.toml` file
for Python projects, or the top-level `.rstcheck.cfg` file otherwise.

Codespell’s default configuration is sufficient, but if extra configuration is
required it should go in the `tool.codespell` section of the top-level
`pyproject.toml` file (in this case ensure the tomli package is installed
alongside codespell) for Python projects. If certain words should be ignored,
they can be added to a top-level `.codespell-ignore-words.txt` file (one word
per line).

Additionally, these linters should be run with pre-commit by adding the
following to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/adrienverge/yamllint.git
    rev: v1.32.0
    hooks:
    - id: yamllint
  - repo: https://github.com/rstcheck/rstcheck
      rev: v6.1.2
      hooks:
      - id: rstcheck
        additional_dependencies:
          - sphinx
          - tomli
  - repo: https://github.com/codespell-project/codespell
    rev: v2.2.4
    hooks:
    - id: codespell
          entry: codespell -I .codespell-ignore-words.txta
      additional_dependencies:
          - tomli
```

Be sure to run `pre-commit autoupdate` to pick up the latest versions of each
tool.

[yamllint]: https://github.com/adrienverge/yamllint
[rstcheck]: https://github.com/rstcheck/rstcheck
[codespell]: https://github.com/codespell-project/codespell

## Python

Additionally, Python based projects should follow these Python-specific
standards.

### Packaging

Projects should use [uv] to manage dependencies, virtualenvs and publish
packages. Running `uv init` should be sufficient to generate the initial
configuration in the top-level `pyproject.toml` file.

Additionally the `uv-pre-commit` hook should be configured to ensure `uv.lock`
gets updated whenever dependencies change:

```yaml
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    rev: 0.10.2
    hooks:
      - id: uv-lock

```

[uv]: https://docs.astral.sh/uv/

### Testing

Tests should run using [Pytest]. While Pytest can run unittest style tests
(class based with setUp/tearDown functions), this is discouraged for new tests.
Instead prefer the standard Pytest style of simple function declarations and
assert statements. Use of fixtures and parameterization are recommended.

Additionally the following extensions are recommended:

* [pytest-mock] - provides the mocker fixture which wraps unittest.mock to
  expose a more powerful mocking interface than the built-in monkeypatch
  fixture.
* [responses] - provides an easy way to mock out (and assert) http requests.

Pytest configuration should live in the top-level `pyproject.toml` file. The
`xfail_strict` option should be set to true:

```toml
[tool.pytest.ini_options]
xfail_strict = true
```

[Pytest]: https://docs.pytest.org/
[pytest-mock]: https://pypi.org/project/pytest-mock/
[responses]: https://pypi.org/project/responses/

#### Coverage

Code coverage should be collected using the [coverage] package. Coverage should
be configured in the top-level `pyproject.toml` file, e.g:

```toml
[tool.coverage.run]
parallel = true
branch = true
source = ["src/{project}"]
```

[coverage]: https://pypi.org/project/coverage/

#### Multiple Python Versions

Tests should be run across all versions of Python the project may be run with
in the wild. The [tox] tool should be used for this. Configuration should live
in a top-level `tox.ini` file and include test environments for each Python
version under test, as well as environments to clean and report code coverage.
For example:

```ini
[tox]
envlist = clean,py{37,38,39,310,311},report

[testenv]
deps = -r{toxinidir}/requirements/test.txt
parallel_show_output = true
usedevelop = true
depends =
    py{37,38,39,310,311}: clean
    report: py{37,38,39,310,311}
commands =
    python --version
    coverage run --context={envname} -p -m pytest -vv {posargs}

[testenv:report]
deps = -r{toxinidir}/requirements/test.txt
skip_install = true
passenv = COVERAGE_REPORT_COMMAND
parallel_show_output = true
commands =
    coverage combine
    {env:COVERAGE_REPORT_COMMAND:coverage report}

[testenv:clean]
deps = -r{toxinidir}/requirements/test.txt
skip_install = true
commands = coverage erase
```

[tox]: https://tox.wiki/

### Formatting and Linting

Projects should use [ruff] for formatting and linting. The default
configuration is recommended, but if extra configuration is necessary (e.g to
exclude files), it should go in the top-level `pyproject.toml` file:

```toml
[tool.ruff]
extend-exclude = [
  "test/data",
  "src/foo",
]
```

Additionally, `ruff` should be configured to run in the pre-commit hook by
adding the following to the top-level `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.5.6
    hooks:
      - id: ruff
        args: ["--fix"]
      - id: ruff-format
```

Be sure to run `pre-commit autoupdate` to pick up the latest version.

[ruff]: https://pypi.org/project/ruff/

#### Lint Rules

Ruff should be configured to run the following lint rules:

* pycodestyle
* pyflakes
* isort
* pylint (convention and error only)
* pyupgrade
* flake8-type-checking

Configuration should live in the top-level `pyproject.toml` file:

```toml
[tool.ruff]
select = [
    "E", "W",         # pycodestyle
    "F",              # pyflakes
    "I",              # isort
    "PLC", "PLE",     # pylint
    "UP",             # pyupgrade
    "TCH",            # flake8-type-checking
]
ignore = [
    "E501",  # let ruff-format handle line-length
]
# change to your minimum supported Python version
target-version = "py38"
```

### Type Checking

Projects should use [Pyright] for type checking. Pyright has advanced type
inference capabilities, so can provide value even on projects that don't have
any type annotations.

While annotations aren't necessary for Pyright to function, providing them
allows both Pyright and other developers to understand the code base in more
depth. As such, annotations should be enforced for new projects.

Configuration for Pyright should live in the top-level `pyproject.toml` file:

```toml
[tool.pyright]
include = "src/<package>"
reportUnknownParameterType = "error"
```

The `reportUnknownParameterType` config enforces type annotations. If enabling
Pyright on an existing project that is missing annotations, it is recommended
to omit this config. In this case, see [Getting Started with Type Checking] for
a recommended incremental upgrade path.

#### Where to Run

Pyright should be run as a Taskcluster task, similar to:

```yaml
type-check:
    description: "Run Pyright type checking against code base"
    worker-type: linux
    worker:
        docker-image: {in-tree: python}
        max-run-time: 300
    run:
        using: run-task
        cwd: '{checkout}'
        use-caches: [checkout, uv]
        command: >-
            uv run pyright
```

While it's possible to run as a [pre-commit hook], this method isn't
recommended as Pyright needs to run in an environment where the project's
dependencies are installed. This means either the dependencies need to be
listed a second time in `pre-commit-config.yaml`, or Pyright needs to be
explicitly told about uv's virtualenv (which varies from person to person
and shouldn't be committed in the config file).

[Pyright]: https://github.com/Microsoft/pyright
[Getting Started with Type Checking]: https://microsoft.github.io/pyright/#/getting-started
[pre-commit hook]: https://microsoft.github.io/pyright/#/ci-integration?id=running-pyright-as-a-pre-commit-hook
