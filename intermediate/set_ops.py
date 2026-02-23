"""Set operations exercises (intermediate).

Implement small functions demonstrating set usage:
- unique_intersection(a, b)
- is_subset(a, b)
- symmetric_difference(a, b)

Functions should accept iterables and return standard Python collections.
"""

from typing import Iterable, Set


def unique_intersection(a: Iterable, b: Iterable) -> Set:
    """Return the intersection of `a` and `b` as a set."""
    raise NotImplementedError()


def is_subset(a: Iterable, b: Iterable) -> bool:
    """Return True if all elements of `a` are in `b`."""
    raise NotImplementedError()


def symmetric_difference(a: Iterable, b: Iterable) -> Set:
    """Return symmetric difference between `a` and `b`."""
    raise NotImplementedError()


if __name__ == "__main__":
    print("Implement set helpers and add tests to validate behavior.")