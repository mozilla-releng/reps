import os
import sys
from argparse import ArgumentParser
from pathlib import Path

from cookiecutter.main import cookiecutter


def init(**kwargs):

    repo = get_repository(os.getcwd())
    root = Path(repo.path)

    # Clean up existing installations if necessary.
    tc_yml = root.joinpath(".taskcluster.yml")
    if tc_yml.is_file():
        if not options["force"]:
            proceed = input(
                "A Taskcluster setup already exists in this repository, "
                "would you like to overwrite it? [y/N]: "
            ).lower()
            while proceed not in ("y", "yes", "n", "no"):
                proceed = input(f"Invalid option '{proceed}'! Try again: ")

            if proceed[0] == "n":
                sys.exit(1)

        tc_yml.unlink()
        tg_dir = root.joinpath("taskcluster")
        if tg_dir.is_dir():
            shutil.rmtree(tg_dir)

    # Populate some defaults from the current repository.
    context = {"project_name": root.name}

    repo_url = repo.get_url()
    if repo.tool == "git" and "github.com" in repo_url:
        context["repo_host"] = "github"
    elif repo.tool == "hg" and "hg.mozilla.org" in repo_url:
        context["repo_host"] = "hgmo"
    else:
        raise RuntimeError(
            "Repository not supported! Taskgraph currently only "
            "supports repositories hosted on Github or hg.mozilla.org."
        )

    # Generate the project.
    cookiecutter(
        options["template"],
        checkout=taskgraph.__version__,
        directory="template",
        extra_context=context,
        no_input=options["no_input"],
        output_dir=root.parent,
        overwrite_if_exists=True,
    )


def run(args=sys.argv[1:]):
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(help="sub-command help")

    init_parser = subparsers.add_parser("init", help="init command help")
    init_parser.
    init_parser.set_defaults(func=init)

    args = vars(parser.parse_args(args))
    func = args.pop("func")
    return func(args)


if __name__ == 'main':
    sys.exit(run())
