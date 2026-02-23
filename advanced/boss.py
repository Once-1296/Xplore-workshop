"""Advanced capstone: boss exercise.

Create a small command-line or Tkinter application that combines concepts
from the other advanced exercises (numpy, pandas, matplotlib, sklearn).

This file is the student-facing entry point for the capstone. Implement
the functions below to integrate dataset loading (from `assets/`), basic
data exploration, a couple of visualizations, and a simple train/evaluate
loop for a regression or classification model.

Instructions (short):
- Load datasets from the `assets/` folder (use the generator script
  `assets/generate_datasets.py` to create sample CSVs).
- Implement `load_data`, `explore_data`, `visualize_data`, and
  `train_and_evaluate` functions.
- You may implement a simple linear model from scratch or use
  scikit-learn if available.

Keep this file as the project entry; keep solutions in a separate
`<githubid>_solutions/` folder when submitting.
"""

from typing import Tuple
import csv


def load_data(path: str) -> Tuple[list, list]:
    """Load CSV data from `path` and return (X, y).

    Keep implementation simple and robust to small formatting issues.
    """
    X = []
    y = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Students: parse row into features and target
            # Example: for a file with 'x' and 'y' columns
            try:
                y.append(float(row.get("y", row.get("label", 0))))
                # collect remaining numeric columns as features
                features = [float(v) for k, v in row.items() if k not in ("y", "label")]
                X.append(features)
            except ValueError:
                # skip rows that don't parse
                continue
    return X, y


def explore_data(X, y):
    """Print a tiny data summary (shape, some stats).

    Keep output human-readable.
    """
    print(f"Rows: {len(X)}")
    if len(X) > 0:
        print(f"Features per row: {len(X[0])}")
    print(f"Target samples: {len(y)}")


def visualize_data(X, y):
    """Placeholder: create a couple of plots using matplotlib.

    Students may import matplotlib and implement plotting here.
    """
    print("Visualization function placeholder - implement plotting here")


def train_and_evaluate(X, y):
    """Train a simple model and print evaluation metrics.

    This can be an implementation of linear regression or use
    scikit-learn if available.
    """
    print("Training placeholder - implement model training and metrics")


if __name__ == "__main__":
    print("This is the advanced capstone entrypoint (boss).")
    print("Run the functions from this module from a script or REPL.")