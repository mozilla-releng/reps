import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Any, List

from cookiecutter.main import cookiecutter

here = Path(__file__).parent
TEMPLATE_DIR = here / "templates"


def available_templates():
    return [path.name for path in TEMPLATE_DIR.iterdir() if path.is_dir()]


def command_new(name: str, template: str, **cookiecutter_args: Any):
    if template not in available_templates():
        print(f"template '{template}' not found!")
        return 1

    if template != "base":
        # The 'base' template will be generated first, and non-base templates
        # then get merged into it. So unless the 'base' template was explicitly
        # specified, ensure we don't error out when the project already exists.
        cookiecutter_args.setdefault("overwrite_if_exists", False)

    template = str(TEMPLATE_DIR / template)
    cookiecutter_args.setdefault("extra_context", {}).setdefault("project_name", name)

    # Generate the project.
    cookiecutter(
        template,
        **cookiecutter_args,
    )


def run(args: List[str] = sys.argv[1:]):
    parser = ArgumentParser()
    parser.add_argument(
        "name", nargs="?", default=None, help="Name of the project to create."
    )
    parser.add_argument(
        "-t",
        "--template",
        default="python",
        choices=available_templates(),
        help="Project template to initialize.",
    )
    parser.add_argument(
        "--no-input", default=False, action="store_true", help="Use defaults"
    )
    parser.set_defaults(func=command_new)

    kwargs = vars(parser.parse_args(args))
    func = kwargs.pop("func")

    if not kwargs["name"] and kwargs["no_input"]:
        parser.error("must specify 'name' when --no-input is used!")
    return func(**kwargs)


if __name__ == "main":
    sys.exit(run())
