"""Class inheritance exercises (intermediate).

Create a small class hierarchy demonstrating inheritance, method overriding,
and use of `super()`.

Tasks:
- Implement a `Person` base class with `name` and `age`.
- Implement an `Employee(Person)` subclass that adds `employee_id` and overrides a method.
- Implement a `Manager(Employee)` subclass that can manage a list of employees.
"""

from typing import List


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Return a greeting string including the name."""
        raise NotImplementedError()


class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def greet(self) -> str:
        """Return a greeting that includes the employee id."""
        raise NotImplementedError()


class Manager(Employee):
    def __init__(self, name: str, age: int, employee_id: str, team: List[Employee] = None):
        super().__init__(name, age, employee_id)
        self.team = team or []

    def add_member(self, employee: Employee):
        """Add an employee to the manager's team."""
        raise NotImplementedError()


if __name__ == "__main__":
    print("Implement the Person/Employee/Manager classes and add tests for inheritance behavior.")