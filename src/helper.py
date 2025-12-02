from shutil import which
import subprocess
import time
from typing import Text

from error import GitError


def get_binary_version(cmd: str, *args: str) -> None | Text:
    """
    Return the version string for an external command like `git --version`.
    Returns None if the binary is not found or fails.
    """

    if which(cmd) is None:
        return None

    try:
        result: subprocess.CompletedProcess[Text] = subprocess.run(
            [cmd, *args], check=True, capture_output=True, text=True, timeout=10
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        return None
    return result.stdout.strip()
