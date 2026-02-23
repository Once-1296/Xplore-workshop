"""List operations exercises (intermediate).

Implement small helper functions that perform common list tasks:
- remove_duplicates(lst)
- flatten(nested_list)
- rotate_list(lst, k)

Each function should be pure (no input prompts) and return values suitable
for unit testing.
"""

from typing import List, Any


def remove_duplicates(lst: List[Any]) -> List[Any]:
    """Return a list with duplicates removed, preserving original order."""
    raise NotImplementedError()


def flatten(nested: List[List[Any]]) -> List[Any]:
    """Flatten a 2-level nested list into a single list."""
    raise NotImplementedError()


def rotate_list(lst: List[Any], k: int) -> List[Any]:
    """Rotate list to the right by k steps and return the result."""
    raise NotImplementedError()


if __name__ == "__main__":
    print("Implement list helpers and add tests to validate behavior.")