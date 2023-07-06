import sys

import {{cookiecutter.__package_name}}  # noqa

def test_{{cookiecutter.__package_name}}():
    assert "{{cookiecutter.__package_name}}" in sys.modules
