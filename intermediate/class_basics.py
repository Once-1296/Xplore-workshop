"""Class basics exercises (intermediate).

Implement a few small classes with methods and simple unit-testable behavior:
- Rectangle: area and perimeter
- BankAccount: deposit/withdraw with simple balance checks
- Counter: simple increment/reset functionality

Students should implement methods and add tests for common edge cases.
"""

from typing import Optional


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return area of the rectangle."""
        raise NotImplementedError()

    def perimeter(self) -> float:
        """Return perimeter of the rectangle."""
        raise NotImplementedError()


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """Deposit amount, return new balance."""
        raise NotImplementedError()

    def withdraw(self, amount: float) -> float:
        """Withdraw amount if sufficient balance, else raise ValueError."""
        raise NotImplementedError()


class Counter:
    def __init__(self, start: int = 0):
        self.value = start

    def increment(self, step: int = 1) -> int:
        """Increment counter by step and return new value."""
        raise NotImplementedError()

    def reset(self, to: int = 0) -> None:
        """Reset counter to `to`."""
        raise NotImplementedError()


if __name__ == "__main__":
    print("This module contains class exercises. Implement the methods and add tests.")