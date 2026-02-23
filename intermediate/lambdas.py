"""Lambda and functional exercises (intermediate).

Implement small utilities that demonstrate lambdas and higher-order functions:
- sort_by_lastname(names)
- apply_transform(lst, func)
- filter_even_squares(nums)

Each function should avoid input() and be easily testable.
"""

from typing import List, Callable, Any


def sort_by_lastname(names: List[str]) -> List[str]:
    """Sort list of full names by their last name using a lambda key."""
    raise NotImplementedError()


def apply_transform(lst: List[Any], func: Callable[[Any], Any]) -> List[Any]:
    """Apply `func` to each element of `lst` and return results as a list."""
    raise NotImplementedError()


def filter_even_squares(nums: List[int]) -> List[int]:
    """Return squares of numbers from `nums` that are even after squaring or before (define behavior in tests)."""
    raise NotImplementedError()


if __name__ == "__main__":
    print("Implement lambda/functional helpers and add tests.")