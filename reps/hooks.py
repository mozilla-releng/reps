import subprocess
from collections import defaultdict
from pathlib import Path

import yaml
from halo import Halo

from reps.console import command_new


HOOKS = defaultdict(list)


def hook(name):
    def wrapper(func):
        HOOKS[name].append(func)
        return func

    return wrapper


def run_hooks(group, items):
    for hook_fn in HOOKS[group]:
        with Halo(f"running {hook_fn.__name__}") as spinner:
            hook_fn(items)
            spinner.succeed(f"{hook_fn.__name__}")


def run(cmd, **kwargs):
    kwargs.setdefault("check", True)
    kwargs.setdefault("stdout", subprocess.PIPE)
    kwargs.setdefault("stderr", subprocess.STDOUT)
    try:
        subprocess.run(cmd, **kwargs)
    except subprocess.CalledProcessError as e:
        print("+ command failed: {' '.join(cmd)}")
        print(e.output)
        raise


@hook("pre-gen-py")
def base_init(items):
    """Generate the 'base' template first."""
    if "_copy_without_render" in items:
        del items["_copy_without_render"]

    command_new(
        items["__project_slug"],
        template="base",
        extra_context=items,
        no_input=True,
        output_dir=str(Path.cwd().parent),
        accept_hooks=False,
        overwrite_if_exists=True,
    )


@hook("post-gen-py")
def merge_pre_commit(items):
    """Update the base pre-commit config with Python-specific tools."""
    with open(".pre-commit-config.yaml", "r") as fh:
        pre_commit_config = yaml.safe_load(fh.read())

    pre_commit_config["repos"].extend(
        [
            {
                "repo": "https://github.com/psf/black",
                "rev": "23.3.0",
                "hooks": [
                    {"id": "black"},
                ],
            },
            {
                "repo": "https://github.com/charliermarsh/ruff-pre-commit",
                "rev": "v0.0.272",
                "hooks": [{"id": "ruff", "args": ["--fix", "--exit-non-zero-on-fix"]}],
            },
        ]
    )

    with open(".pre-commit-config.yaml", "w") as fh:
        fh.write(yaml.safe_dump(pre_commit_config))


@hook("post-gen-py")
def add_poetry_dependencies(items):
    run(
        [
            "poetry",
            "add",
            "--group=test",
            "coverage",
            "pytest",
            "pytest-mock",
            "responses",
            "tox",
        ]
    )
    run(
        [
            "poetry",
            "add",
            "--group=docs",
            "sphinx<7",
            "sphinx-autobuild",
            "sphinx-book-theme",
        ]
    )


@hook("post-gen-py")
@hook("post-gen-base")
def git_init(items):
    run(["git", "init"])
    run(["git", "checkout", "-b", "main"])
    run(
        [
            "git",
            "remote",
            "add",
            "origin",
            f"git@github.com:{items['github_slug']}.git",
        ]
    )


@hook("post-gen-py")
@hook("post-gen-base")
def pre_commit_autoupdate(items):
    run(["pre-commit", "autoupdate"])


@hook("post-gen-py")
@hook("post-gen-base")
def lock_taskgraph_requirements(items):
    run(["pip-compile", "requirements.in", "--generate-hashes"], cwd="taskcluster")


@hook("post-gen-base")
def taskgraph_init(items):
    run(["taskgraph", "init"])
