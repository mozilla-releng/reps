## 0.5.0 (2026-08-18)

### Feat

- use matrix transforms to handle many Python versions
- switch pull request policy to public (#108)
- use shared hook to run pre-commit
- enable 'check-merge-conflict' pre-commit hook

### Fix

- codecov task worker-type
- extra quote in .taskcluster.yml
- stop using variable for UV_VERSION
- use debian-slim as base for fetch image
- indentation in .taskcluster.yml
- use proper decision worker pool
- use base repo when finding project name for pull requests (#109)
- renovate.json configuration (round 2) (#96)
- change lockFileMaintenance schedule to match main schedule (#95)
- renovate preset syntax (#94)
- **bug 2043228**: allow renovate PRs to be created at any hour (#92)
- invalid json in renovate config

## 0.4.1 (2026-02-17)

### Feat

- add 'uv-pre-commit' hook to template

### Fix

- use 'pre-commit' Github action instead of pre-commit.ci
- automatically set up origin remote
- add pyright to dev dependencies

### Refactor

- copier vcs commands for legibility

## 0.4.0 (2026-02-09)

### Feat

- pin to Taskgraph 18.1.0
- switch from cookiecutter to copier
- **renovate**: group github action updates together (#65)
- **renovate**: don't group major updates for JS and docker updates together (#63)
- add renovatebot support (#62)
- **python**: switch Python spec from poetry to uv
- **python**: switch from black to ruff-format for formatting
- add type checking with Pyright to the standard

### Fix

- update python Dockerfile
- ensure Decision task works with `taskgraph-decision` image
- include digest only updates in Docker and GH Action groupings
- remove unused 'ci' section from .pre-commit-config.yaml
- **python**: update template for Taskgraph 7+
- **python**: set pre-commit autoupdate schedule to monthly
- **dependencies**: py38 upstream dependencies and relock packages (#35)
- **python**: typo in .pre-commit-config.yaml

## 0.3.6 (2023-11-21)

### Fix

- **python**: scope checkout caches to the specific project
- **python**: update min and max Python versions
- **python**: point 'ruff' at new repo
- ensure 'package_name' always uses underscores
- **python**: Don't put codecov secret under 'level-3' bucket
- **python**: Update secrets path to new trust-domain-scopes standard
- use constraints in 'add_poetry_dependencies' hook to avoid incompatible versions
- properly format failures in 'hooks.run'
- **python**: switch the template to the 'public_restricted' policy
- **python**: enable Taskcluster Github's 'autoCancelPreviousChecks'

## 0.3.5 (2023-07-11)

### Fix

- **python**: remove 'mermaid' extension

## 0.3.4 (2023-07-10)

### Fix

- **hooks**: remove leftover debug statement

## 0.3.3 (2023-07-10)

### Fix

- **python**: use ruamel.yaml for merging pre-commit
- **python**: add missing .gitignore file

## 0.3.2 (2023-07-10)

### Feat

- adjust min supported Python to 3.8
- add a flag to run without user input (accepting defaults)

### Fix

- **python**: leave 'base_ref' empty if not passed in by Github

## 0.3.1 (2023-07-07)

### Fix

- **hooks**: strip 'running' on hook success
- **python**: whitespace lint errors
- **base**: populate .yamllint config

## 0.3.0 (2023-07-07)

### Feat

- **hooks**: suppress command output unless there's a failure

### Fix

- use 'halo' for progress spinners

## 0.2.0 (2023-07-06)

### Feat

- **python**: add an empty package
- create 'base' and 'python' templates
- create a basic command line interface

### Fix

- **python**: set Python versions in the docker image rather than at task runtime
- **python**: fix codecov-upload command
- **python**: chown HOME in Python docker image
- **python**: fix unit test command line to run tox
- **python**: use proper key for externals
- **python**: set level properly in .taskcluster.yml
- **python**: setup poetry in python docker image
- **python**: install test dependencies in test task
- 'base_init' hook now correctly passes in context
- **python**: fix codecov-upload worker-type and secret scopes
- **python**: make max python version consistent with min version
- **python**: adjust secrets path
- **python**: use latest decision image
- **python**: use 'short_{base|head}_ref' in .tc.yml
- **python**: remove treeherder; tweak worker-type
- **python**: add Taskgraph requirements
- run tasks on all branches
- add Docker dirs for fetch and python images
- **python**: actually put package in project dir
