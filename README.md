# Release Engineering Project Standard

This repository:

1. Defines the standard tools and workflows that Mozilla Release Engineering
   endeavours to use across its projects.
2. Implements a `reps` binary that can be used to bootstrap new projects based
   on the defined standard.

## Usage

The `reps` tool can be used to bootstrap new projects that conform to this
standard. It is recommended to install it with [pipx](https://github.com/pypa/pipx):

```bash
pipx install releng-project-standard
```

Then run:

```bash
reps new
```

and fill out the prompts. By default, the `python` project template is used.
You may optionally specify a different template to use with the `-t/--template` flag:

```bash
reps new -t base
```

Available templates can be found in the
[templates directory](https://github.com/mozilla-releng/reps/tree/main/src/reps/templates).
