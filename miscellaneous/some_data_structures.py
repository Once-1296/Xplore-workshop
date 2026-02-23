"""Data structure usage exercises (miscellaneous).

Implement small helper functions demonstrating:
- stack (LIFO)
- queue (FIFO)
- heap (min-heap using heapq)
- map/dict usage

Provide a `run_tests()` helper that runs small smoke tests using
arrays from `assets/algo_arrays.json`.
"""

from typing import List, Any, Dict
import heapq
import json
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"


def stack_push_pop(seq: List[Any]) -> List[Any]:
    """Push items from `seq` onto a stack and pop them all; return popped order."""
    raise NotImplementedError()


def queue_enqueue_dequeue(seq: List[Any]) -> List[Any]:
    """Enqueue items from `seq` and dequeue them all; return dequeued order."""
    raise NotImplementedError()


def heap_push_pop(seq: List[int]) -> List[int]:
    """Push numbers into a min-heap and pop them to return sorted order."""
    raise NotImplementedError()


def map_count(seq: List[Any]) -> Dict[Any, int]:
    """Return a frequency map (dict) for elements in `seq`."""
    raise NotImplementedError()


def run_tests():
    """Run small smoke tests using `assets/algo_arrays.json` (if present)."""
    path = ASSETS / "algo_arrays.json"
    if not path.exists():
        print("No algo_arrays.json found in assets. Run assets/generate_datasets.py first.")
        return
    data = json.loads(path.read_text())
    print("Loaded test arrays. Extend run_tests with assertions for each helper.")


if __name__ == "__main__":
    run_tests()