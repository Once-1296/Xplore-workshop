"""Pandas basics exercises (advanced).

Tasks:
- Load CSV into a DataFrame
- Implement filtering, grouping and aggregation functions
- Provide a function that handles missing values

Each function should accept either a DataFrame or a path to a CSV and return
a DataFrame or a derived value.
"""

from typing import Optional


def load_csv(path: str):
    """Load a CSV from `path` and return a pandas DataFrame.

    If pandas is not available, students can implement a simple CSV loader.
    """
    raise NotImplementedError()


def drop_missing(df, how: str = "any"):
    """Drop missing values from DataFrame `df` and return cleaned DataFrame.

    `how` is passed to DataFrame.dropna.
    """
    raise NotImplementedError()


def group_and_aggregate(df, group_by: str, agg_col: str):
    """Group by `group_by` column and return aggregate (mean) of `agg_col`.
    """
    raise NotImplementedError()


if __name__ == "__main__":
    print("This module contains advanced pandas exercises. Implement the functions.")