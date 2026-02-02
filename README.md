[![Task Status](https://firefox-ci-tc.services.mozilla.com/api/github/v1/repository/mozilla-releng/reps/main/badge.svg)](https://firefox-ci-tc.services.mozilla.com/api/github/v1/repository/mozilla-releng/reps/main/latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/mozilla-releng/reps/main.svg)](https://results.pre-commit.ci/latest/github/mozilla-releng/reps/main)
[![License](https://img.shields.io/badge/license-MPL%202.0-orange.svg)](http://mozilla.org/MPL/2.0)

# Release Engineering Project Standard

This repository:

1. Defines the standard tools and workflows that Mozilla Release Engineering
   endeavours to use across its projects.
2. Provides a [copier](https://copier.readthedocs.io/en/latest/) template that
   can be used to bootstrap new projects based on the defined standard.

## Project Standard

Please see
[STANDARD.md](https://github.com/mozilla-releng/reps/blob/main/STANDARD.md) for
the REPS definition.

## Usage

The `copier` template can be used to bootstrap new projects that conform to this
standard. First install copier:

```bash
uv tool install copier
```

Then run:

```bash
copier copy --trust mozilla-releng/reps my-project
```

and fill out the prompts. A new project will be bootstrapped under the `my-project`
directory.

You can also update a project with the latest changes to the template:

```bash
cd my-project
copier update
```
