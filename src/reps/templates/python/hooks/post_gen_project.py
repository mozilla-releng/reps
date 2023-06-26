from collections import OrderedDict

from reps.hooks import run_hooks


items = {{cookiecutter}}
run_hooks("post-gen-py", items)
