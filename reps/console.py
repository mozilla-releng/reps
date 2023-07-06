import sys
from argparse import ArgumentParser
from pathlib import Path

from cookiecutter.main import cookiecutter

here = Path(__file__).parent
TEMPLATE_DIR = here / "templates"


def available_templates():
    return [path.name for path in TEMPLATE_DIR.iterdir() if path.is_dir()]


def command_new(name, template, **cookiecutter_args):
    if template not in available_templates():
        print(f"template '{template}' not found!")
        return 1

    if template != "base":
        # The 'base' template will be generated first, and non-base templates
        # then get merged into it. So unless the 'base' template was explicitly
        # specified, ensure we don't error out when the project already exists.
        cookiecutter_args.setdefault("overwrite_if_exists", False)

    template = TEMPLATE_DIR / template
    cookiecutter_args.setdefault("extra_context", {}).setdefault("project_name", name)

    # Generate the project.
    cookiecutter(
        str(template),
        **cookiecutter_args,
    )


def run(args=sys.argv[1:]):
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
    parser.set_defaults(func=command_new)

    kwargs = vars(parser.parse_args(args))
    func = kwargs.pop("func")
    return func(**kwargs)


if __name__ == "main":
    sys.exit(run())
