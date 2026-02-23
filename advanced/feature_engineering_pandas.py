"""Feature engineering and basic EDA with pandas/seaborn (advanced).

Implement functions that transform and prepare a pandas DataFrame for ML:
- add_interaction_terms(df, cols)
- encode_categorical(df, column)
- normalize_columns(df, cols)
- impute_missing(df, strategy)
- correlation_matrix(df)

Students may use pandas and seaborn if available; otherwise implement
small equivalents using the csv module and simple Python lists/dicts.
"""

from typing import Any, Sequence


def add_interaction_terms(df: Any, cols: Sequence[str]):
    """Add pairwise interaction columns for the listed `cols` and return df."""
    raise NotImplementedError()


def encode_categorical(df: Any, column: str):
    """Return df with `column` label-encoded or one-hot encoded."""
    raise NotImplementedError()


def normalize_columns(df: Any, cols: Sequence[str]):
    """Normalize columns (min-max or z-score) and return transformed df."""
    raise NotImplementedError()


def impute_missing(df: Any, strategy: str = "mean"):
    """Impute missing values according to `strategy` (mean/median/most_frequent)."""
    raise NotImplementedError()


def correlation_matrix(df: Any):
    """Return a correlation matrix (DataFrame or nested lists)."""
    raise NotImplementedError()


if __name__ == "__main__":
    print("This module contains feature engineering exercises. Implement the functions.")