# import os
from pathlib import Path
import subprocess
from typing import Any

from src.error import GitError


class Serve_Res(dict):
    def __init__(self, *args, **kwargs) -> None:
        # custome values that can be included
        custom: dict = {}

        defaults: dict = {
            "error_str": None,
            "custom_res_str": None,
            "return_code": None,
            "status": None,
            "stdout": None,
            "stderr": None,
        }
        defaults.update(dict(*args, **kwargs))

        # default template keys
        super().__init__(defaults)

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError(name) from exc

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"):
            return super().__setattr__(name, value)
        self[name] = value


class Actions:
    DEFAULT_REPO_DIR: Path = Path("/srv/git")
    GIT_SUFFIX: str = ".git"

    def __init__(self, REPO_DIR: None = None, DEBUG: bool = True) -> None:
        if REPO_DIR is None:
            self.REPO_DIR: Path = self.DEFAULT_REPO_DIR
        else:
            self.REPO_DIR = Path(REPO_DIR)

        self.DEBUG: bool = DEBUG

    def create_repo(self, repo_name: str) -> Any:
        if not repo_name.endswith(".git"):
            repo_name += self.GIT_SUFFIX

        path: Path = self.REPO_DIR
        path = path.joinpath(repo_name)

        res: Serve_Res = Serve_Res()

        if path.exists():
            res.error_str = f"The repository {repo_name} already exists. Please choose a new repository name."
            res.status = "failed"
            return res

        try:
            result: subprocess.CompletedProcess[str] = subprocess.run(
                ["git", "init", "--bare", path],
                check=True,
                text=True,
                capture_output=True,
            )
            res.status = "success"
            res.stdout = result.stdout.strip()
            return res

        except subprocess.CalledProcessError as e:
            res.status = "failed"
            res.stderr = e.stderr.strip()
            res.return_code = e.returncode
            res.error_str = "Creation of a new repository failed"

            if self.DEBUG is True:
                print(f"Command failed with return code {e.returncode}")
                print(f"Error output: {e.stderr}")
                return res
            else:
                return res


if __name__ == "__main__":
    pass
