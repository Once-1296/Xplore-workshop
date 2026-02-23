"""Sklearn exercises (advanced).

Provide two example pipelines:
- a preprocessing + regression pipeline
- a preprocessing + classification pipeline

Students may use scikit-learn if available, otherwise implement simple
train/test split and a basic model.
"""

from typing import Tuple


def load_ml_datasets():
    """Return paths or loaded datasets for the regression and classification tasks.

    Expected return format: (regression_path_or_data, classification_path_or_data)
    """
    raise NotImplementedError()


def simple_train_test_split(X, y, test_fraction: float = 0.2) -> Tuple[list, list, list, list]:
    """Split X, y into train/test lists.
    """
    raise NotImplementedError()


def evaluate_regression(preds, targets):
    """Return a dict with regression metrics (mse, mae, r2 optional).
    """
    raise NotImplementedError()


def evaluate_classification(preds, targets):
    """Return a dict with accuracy, precision, recall (simple implementations ok).
    """
    raise NotImplementedError()


if __name__ == "__main__":
    print("This module contains sklearn-related exercises. Implement datasets and pipelines.")