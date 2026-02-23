"""Numpy basics exercises (advanced).

Implement functions demonstrating common NumPy tasks:
- shape and reshaping
- broadcasting
- linspace and random generation
- basic statistical functions (mean, std, median)
- a small example using trigonometric functions

Provide small, testable functions below that return NumPy arrays or scalars.
"""

from typing import Tuple


def create_sequence(start: float, stop: float, num: int):
    """Return a 1-D sequence of `num` floats between start and stop (inclusive).

    Expected return type: a list or numpy array-like sequence.
    """
    # Student: implement using numpy.linspace (or pure Python if numpy is unavailable)
    raise NotImplementedError()


def random_matrix(rows: int, cols: int, seed: int = 0):
    """Return a rows x cols matrix of random floats.

    Use a seed for reproducibility.
    """
    raise NotImplementedError()


def reshape_example(arr, new_shape: Tuple[int, ...]):
    """Reshape arr into new_shape and return it.

    If reshaping is not possible, raise a ValueError.
    """
    raise NotImplementedError()


def statistics(arr):
    """Return a dict with mean, median, std of numeric array-like `arr`.

    e.g. {"mean": ..., "median": ..., "std": ...}
    """
    raise NotImplementedError()


if __name__ == "__main__":
    print("This module contains advanced numpy exercises. Implement the functions and run unit tests.")