"""Text (TXT) file CRUD helpers (intermediate).

All file operations target the `assets/` directory so students can run
and reset test data easily. Functions are small and testable.
"""

from pathlib import Path
from typing import List

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def write_text(filename: str, content: str) -> Path:
    """Write `content` to `assets/filename` (overwrite) and return Path."""
    p = ASSETS / filename
    p.write_text(content, encoding="utf-8")
    return p


def read_text(filename: str) -> str:
    """Read and return text from `assets/filename`. Raises FileNotFoundError if missing."""
    p = ASSETS / filename
    return p.read_text(encoding="utf-8")


def append_text(filename: str, content: str) -> Path:
    """Append `content` to `assets/filename`, creating it if necessary."""
    p = ASSETS / filename
    with p.open("a", encoding="utf-8") as f:
        f.write(content)
    return p


def overwrite_line(filename: str, line_no: int, new_line: str) -> bool:
    """Replace a specific line (0-indexed) in the file. Return True on success."""
    p = ASSETS / filename
    if not p.exists():
        raise FileNotFoundError(p)
    lines = p.read_text(encoding="utf-8").splitlines()
    if line_no < 0 or line_no >= len(lines):
        raise IndexError("line_no out of range")
    lines[line_no] = new_line
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


if __name__ == "__main__":
    demo = "Hello students!\nThis is a demo file.\n"
    write_text("demo.txt", demo)
    print(read_text("demo.txt"))