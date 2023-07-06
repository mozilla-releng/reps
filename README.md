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
