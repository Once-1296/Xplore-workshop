"""Linear algebra with NumPy (advanced).

Implement small functions that demonstrate common linear algebra tasks:
- random_matrix(rows, cols, seed)
- matrix_inverse(A)
- solve_linear_system(A, b)
- eigenvalues(A)
- matrix_determinant(A)

If NumPy is unavailable, students may implement simplified pure-Python
versions for small sizes for learning purposes.
"""

from typing import Any, Sequence, Tuple


def random_matrix(rows: int, cols: int, seed: int = 0):
    """Return a random matrix-like object (preferably a numpy.ndarray).

    Use `seed` for reproducibility.
    """
    raise NotImplementedError()


def matrix_inverse(A: Any):
    """Return inverse of matrix A. If A is singular, raise a ValueError.

    Accept NumPy arrays or list-of-lists for student implementations.
    """
    raise NotImplementedError()


def solve_linear_system(A: Any, b: Sequence[float]):
    """Solve Ax = b and return x.

    Raise ValueError for singular or incompatible inputs.
    """
    raise NotImplementedError()


def eigenvalues(A: Any):
    """Return eigenvalues of A as a sequence.

    If NumPy is available, use numpy.linalg.eigvals.
    """
    raise NotImplementedError()


def matrix_determinant(A: Any):
    """Return determinant of matrix A.

    Accept NumPy arrays or list-of-lists.
    """
    raise NotImplementedError()


if __name__ == "__main__":
    print("This module contains linear algebra exercises. Implement the functions.")