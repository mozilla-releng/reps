## 0.4.0 (2024-02-02)

### Feat

- add type checking with Pyright to the standard

### Fix

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
