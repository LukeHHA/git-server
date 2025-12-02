# import os
from pathlib import Path
import subprocess
from typing import Any

from src.error import GitError


class Actions:
    DEFAULT_REPO_DIR: Path = Path("/srv/git")
    GIT_SUFFIX: str = ".git"

    def __init__(self, REPO_DIR: None = None) -> None:
        if REPO_DIR is None:
            self.REPO_DIR: Path = self.DEFAULT_REPO_DIR
        else:
            self.REPO_DIR = Path(REPO_DIR)

    def server_init(self) -> str:
        path: Path = Path("/srv/git")
        if not path.exists():
            path.mkdir()
            return "*** Created path /srv/git/ ***"
        else:
            return "/srv/ does not exist on the host system."

    def create_repo(self, repo_name: str) -> Any:
        if not repo_name.endswith(".git"):
            repo_name += self.GIT_SUFFIX

        path: Path = self.REPO_DIR
        path = path.joinpath(repo_name)

        if path.exists():
            res: str = (
                "This repository already exists. Please choose a new repository name."
            )
            return res

        result: subprocess.CompletedProcess[str] = subprocess.run(
            ["git", "init", "--bare", path], check=True, text=True
        )

        if result.returncode != 0:
            raise GitError(result.args, result.returncode, result.stdout, result.stderr)
        return result.stdout


if __name__ == "__main__":
    pass
