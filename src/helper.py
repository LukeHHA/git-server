from shutil import which
from pathlib import Path
import subprocess
import time
from typing import Text

from src.error import GitError


class Serve_Helper:
    DEFAULT_PATH: Path = Path("/srv/git")

    @staticmethod
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

    @staticmethod
    def pre_check():
        if not Serve_Helper.DEFAULT_PATH.exists() is True:
            return False
        return True
