[![Task Status](https://firefox-ci-tc.services.mozilla.com/api/github/v1/repository/mozilla-releng/reps/main/badge.svg)](https://firefox-ci-tc.services.mozilla.com/api/github/v1/repository/mozilla-releng/reps/main/latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/mozilla-releng/reps/main.svg)](https://results.pre-commit.ci/latest/github/mozilla-releng/reps/main)
[![Code Coverage](https://codecov.io/gh/mozilla-releng/reps/branch/main/graph/badge.svg?token=GJIV52ZQNP)](https://codecov.io/gh/mozilla-releng/reps)
[![Documentation Status](https://readthedocs.org/projects/reps/badge/?version=latest)](https://reps.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/license-MPL%202.0-orange.svg)](http://mozilla.org/MPL/2.0)

# Release Engineering Project Standard

This repository:

1. Defines the standard tools and workflows that Mozilla Release Engineering
   endeavours to use across its projects.
2. Implements a `reps` binary that can be used to bootstrap new projects based
   on the defined standard.

## Project Standard

Please see
[STANDARD.md](https://github.com/mozilla-releng/reps/blob/main/STANDARD.md) for
the REPS definition.

## Usage

The `reps` tool can be used to bootstrap new projects that conform to this
standard. It is recommended to install and run it with
[pipx](https://github.com/pypa/pipx) (so the most up to date version is always
used):

```bash
pipx run reps-new
```

and fill out the prompts. By default, the `python` project template is used.
You may optionally specify a different template to use with the `-t/--template` flag:

```bash
pipx run reps-new -t base
```

Available templates can be found in the
[templates directory](https://github.com/mozilla-releng/reps/tree/main/reps/templates).
