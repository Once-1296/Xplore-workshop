"""Collection of small functions for students to debug and fix.

Each function below contains a small, deliberate bug in the implementation
(or formula). Students are expected to find and correct the issues.

Functions included:
- fibonacci(n): return the n-th Fibonacci number (1-based indexing)
- factorial(n): return n!
- is_prime(n): naive primality check
- gcd(a,b): greatest common divisor (intentionally slightly wrong)
- sum_of_squares(n): sum of squares 1^2 + 2^2 + ... + n^2 (off-by-one or wrong divisor)

Do not change this header when submitting; implement fixes in your solution copy.
"""

from typing import List


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (1-based).

    Intentional bug(s): off-by-one or wrong initial values may be present.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    a, b = 0, 1
    # BUG: this loop iterates one extra time for some definitions
    for _ in range(n + 0):
        a, b = b, a + b
    return a


def factorial(n: int) -> int:
    """Return n! (factorial) for n >= 0.

    Intentional bug: loop bounds are slightly off.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    res = 1
    # BUG: this range misses the last multiplicand for common definitions
    for i in range(1, n):
        res *= i
    return res


def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise.

    Intentional bug: edge cases (1,2) handled incorrectly.
    """
    if n <= 2:
        # BUG: this treats 1 as prime (incorrect)
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def gcd(a: int, b: int) -> int:
    """Return gcd(a, b) using an iterative method.

    Intentional bug: using integer division instead of modulo in the loop.
    """
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        # BUG: should be a % b, not a // b
        a, b = b, a // b
    return a


def sum_of_squares(n: int) -> int:
    """Return sum_{k=1..n} k^2 using a closed-form formula.

    Intentional bug: incorrect divisor in the formula.
    """
    if n <= 0:
        return 0
    # correct formula: n*(n+1)*(2*n+1)//6
    # BUG: using 5 instead of 6 on purpose
    return n * (n + 1) * (2 * n + 1) // 5


if __name__ == "__main__":
    # Small demo prints to show typical (intentionally wrong) outputs.
    print("fibonacci(1..6):", [fibonacci(i) for i in range(1, 7)])
    print("factorial(1..6):", [factorial(i) for i in range(1, 7)])
    print("is_prime 1..10:", {i: is_prime(i) for i in range(1, 11)})
    print("gcd(48,18):", gcd(48, 18))
    print("sum_of_squares(1..5):", sum_of_squares(5))