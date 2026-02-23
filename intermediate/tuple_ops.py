"""Tuple operations exercises (intermediate).

Implement tuple-related helpers:
- tuple_to_list(t)
- swap_first_last(t)
- count_in_tuple(t, value)

Return types should be appropriate (lists for converted tuples, tuples for swaps).
"""

from typing import Tuple, Any, List


def tuple_to_list(t: Tuple[Any, ...]) -> List[Any]:
    """Convert tuple `t` to a list and return it."""
    raise NotImplementedError()


def swap_first_last(t: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """Return a new tuple with the first and last elements swapped."""
    raise NotImplementedError()


def count_in_tuple(t: Tuple[Any, ...], value: Any) -> int:
    """Return how many times `value` appears in `t`."""
    raise NotImplementedError()


if __name__ == "__main__":
    print("Implement tuple helpers and add tests to validate behavior.")