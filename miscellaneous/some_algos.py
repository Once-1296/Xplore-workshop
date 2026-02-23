"""Algorithm practice exercises.

Implement the following algorithms (each should be testable):
- binary_search(sorted_list, target)
- sliding_window_max(arr, k)
- two_pointers_pair_sum(arr, target)
- simple DFS and BFS traversals for an adjacency list

Also provide a `run_tests()` helper that exercises the implementations.
"""

from collections import deque
from typing import List, Dict


def binary_search(arr: List[int], target: int) -> int:
    """Return index of target in sorted arr, or -1 if not found."""
    raise NotImplementedError()


def sliding_window_max(arr: List[int], k: int) -> List[int]:
    """Return list of maximums for each sliding window of size k."""
    raise NotImplementedError()


def two_pointers_pair_sum(arr: List[int], target: int) -> List[int]:
    """Return a pair of indices (i,j) such that arr[i]+arr[j] == target or [] if none.

    `arr` is assumed to be sorted for the two-pointer technique.
    """
    raise NotImplementedError()


def dfs(adj: Dict[int, List[int]], start: int) -> List[int]:
    """Return list of nodes in DFS visit order starting from `start`."""
    raise NotImplementedError()


def bfs(adj: Dict[int, List[int]], start: int) -> List[int]:
    """Return list of nodes in BFS visit order starting from `start`."""
    raise NotImplementedError()


def run_tests():
    """Simple smoke tests for the exercises. Students should extend these.

    The repo also includes a dataset generator (`assets/generate_datasets.py`) for
    test-case generation.
    """
    print("Run and extend tests for algorithm exercises.")


if __name__ == "__main__":
    run_tests()