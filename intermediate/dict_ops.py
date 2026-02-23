"""Dictionary operations exercises (intermediate).

Implement helpers:
- invert_dict(d): invert keys and values (assume values are hashable)
- merge_dicts(dicts): merge list of dicts into single dict (later keys override)
- count_keys_with_prefix(d, prefix): count keys starting with prefix
"""

from typing import Dict, Iterable, Any, List


def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return a dict where keys and values are swapped."""
    raise NotImplementedError()


def merge_dicts(dicts: Iterable[Dict[Any, Any]]) -> Dict[Any, Any]:
    """Merge an iterable of dicts into a single dict. Later dicts override earlier ones."""
    raise NotImplementedError()


def count_keys_with_prefix(d: Dict[str, Any], prefix: str) -> int:
    """Count how many keys in d start with `prefix`."""
    raise NotImplementedError()


if __name__ == "__main__":
    print("Implement dict helpers and add tests to validate behavior.")