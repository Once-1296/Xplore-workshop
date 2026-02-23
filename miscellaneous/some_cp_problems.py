"""Competitive programming practice (miscellaneous).

Provide function stubs for a few simple problems. Students should implement
logic and the I/O wrapper. `run_tests()` can be used to run internal testcases
stored under `assets/`.
"""

from pathlib import Path
from typing import List
import json

ASSETS = Path(__file__).resolve().parent.parent / "assets"


def problem_sum_pairs(arr: List[int], target: int) -> List[int]:
    """Return indices (i,j) of a pair that sums to target, or [] if none.

    Students: implement an O(n) solution using a hash map.
    """
    raise NotImplementedError()


def problem_max_subarray(arr: List[int]) -> int:
    """Return maximum subarray sum (Kadane's algorithm).

    Students: implement and optimize for negative-only arrays.
    """
    raise NotImplementedError()


def run_tests():
    """Run small preset tests from `assets/cp_tests.json` if present.

    Create or extend `assets/cp_tests.json` for additional testcases.
    """
    path = ASSETS / "cp_tests.json"
    if not path.exists():
        print("No cp_tests.json found in assets. Create one to run automated tests.")
        return
    data = json.loads(path.read_text())
    print("Loaded CP tests. Students should implement functions and re-run this.")


if __name__ == "__main__":
    run_tests()