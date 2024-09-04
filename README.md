[![Task Status](https://firefox-ci-tc.services.mozilla.com/api/github/v1/repository/mozilla-releng/reps/main/badge.svg)](https://firefox-ci-tc.services.mozilla.com/api/github/v1/repository/mozilla-releng/reps/main/latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/mozilla-releng/reps/main.svg)](https://results.pre-commit.ci/latest/github/mozilla-releng/reps/main)
[![Code Coverage](https://codecov.io/gh/mozilla-releng/reps/branch/main/graph/badge.svg?token=GJIV52ZQNP)](https://codecov.io/gh/mozilla-releng/reps)
[![PyPI version](https://badge.fury.io/py/reps-new.svg)](https://badge.fury.io/py/reps-new)
[![License](https://img.shields.io/badge/license-MPL%202.0-orange.svg)](http://mozilla.org/MPL/2.0)

# Release Engineering Project Standard

This repository:

1. Defines the standard tools and workflows that Mozilla Release Engineering
   endeavours to use across its projects.
2. Implements a `reps-new` binary that can be used to bootstrap new projects based
   on the defined standard.

## Project Standard

Please see
[STANDARD.md](https://github.com/mozilla-releng/reps/blob/main/STANDARD.md) for
the REPS definition.

## Usage

The `reps-new` tool can be used to bootstrap new projects that conform to this
standard. It is recommended to install and run it with
[uvx](https://docs.astral.sh/uv/guides/tools/) (so the most up to date version
is always used). First [install
uv](https://docs.astral.sh/uv/getting-started/installation/), then run:

```bash
uvx reps-new
```

and fill out the prompts. By default, the `python` project template is used.
You may optionally specify a different template to use with the `-t/--template` flag:

```bash
uvx reps-new -t base
```

Available templates can be found in the
[templates directory](https://github.com/mozilla-releng/reps/tree/main/reps/templates).
