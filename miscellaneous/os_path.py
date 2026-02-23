"""OS and pathlib exercises (miscellaneous).

Implement small utilities using `os` and `pathlib`:
- list_files(dir_path)
- make_nested_dirs(dir_path)
- safe_remove(path)  # should NOT remove outside a safe base during tests

Avoid destructive operations; implement safety checks in `safe_remove`.
"""

from pathlib import Path
from typing import List


def list_files(dir_path: str) -> List[str]:
    """Return a list of filenames (not full paths) in dir_path."""
    raise NotImplementedError()


def make_nested_dirs(dir_path: str):
    """Create nested directories and return a Path object for the final dir."""
    raise NotImplementedError()


def safe_remove(path: str, base: str = ".") -> bool:
    """Remove `path` only if it is inside `base` directory. Return True if removed.

    This function should prevent accidental removal outside the `base` path.
    """
    raise NotImplementedError()


if __name__ == "__main__":
    print("Implement os/path utilities and add tests. Do NOT call safe_remove on important data.")