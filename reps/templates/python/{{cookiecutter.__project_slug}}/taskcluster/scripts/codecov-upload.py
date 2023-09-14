import os
import stat
import subprocess
from pathlib import Path

import requests

FETCHES_DIR = Path(os.environ["MOZ_FETCHES_DIR"])
SECRET_BASEURL_TPL = "http://taskcluster/secrets/v1/secret/{}"


def fetch_secret(secret_name):
    """Retrieves the given taskcluster secret"""
    secret_url = SECRET_BASEURL_TPL.format(secret_name)
    r = requests.get(secret_url)
    r.raise_for_status()
    return r.json()["secret"]


token = fetch_secret("{{cookiecutter.__codecov_secrets_path}}")["token"]
uploader = FETCHES_DIR / "codecov"
uploader.chmod(uploader.stat().st_mode | stat.S_IEXEC)
subprocess.run(
    [str(uploader), "-t", token, "-f", str(FETCHES_DIR / "coverage.xml")], check=True
)
