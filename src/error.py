class GitError(RuntimeError):
    def __init__(
        self, args: list[str], returncode: int, stdout: str, stderr: str
    ) -> None:
        self.args_run: list[str] = args
        self.returncode: int = returncode
        self.stdout: str = stdout
        self.stderr: str = stderr
        super().__init__(
            f"git {' '.join(args)} failed with code {returncode}: {stderr.strip()}"
        )
