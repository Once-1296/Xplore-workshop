"""Small dataset generator to create CSVs used by exercises.

This script writes sample files into the same `assets/` directory:
- students.csv: small table of names, age, grade, score
- ml_regression.csv: simple linear regression dataset with noise
- ml_classification.csv: synthetic 2-feature classification dataset
- algo_arrays.json: JSON with arrays useful for algorithm tests

Usage:
    python assets/generate_datasets.py

No external dependencies required (uses only stdlib).
"""

import csv
import json
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def generate_students(path: Path):
    rows = [
        ("Alicia", 21, "A", 88.5),
        ("Ben", 19, "B", 72.0),
        ("Carmen", 22, "A", 91.2),
        ("Dev", 20, "C", 60.5),
        ("Eli", 23, "B", 75.3),
    ]
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "grade", "score"])
        writer.writerows(rows)


def generate_regression(path: Path, n=200, seed=0):
    random.seed(seed)
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x1", "x2", "y"])
        for i in range(n):
            x1 = random.uniform(-10, 10)
            x2 = random.uniform(-5, 5)
            # simple linear relationship with noise
            y = 3.5 * x1 - 1.2 * x2 + random.gauss(0, 2.0)
            writer.writerow([f"{x1:.5f}", f"{x2:.5f}", f"{y:.5f}"])


def generate_classification(path: Path, n=200, seed=1):
    random.seed(seed)
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x1", "x2", "label"])
        for i in range(n):
            x1 = random.uniform(-3, 3)
            x2 = random.uniform(-3, 3)
            # simple non-linear decision boundary
            label = 1 if (x1 * x1 + x2 * x2) > 4 else 0
            # add a tiny noise flip
            if random.random() < 0.05:
                label = 1 - label
            writer.writerow([f"{x1:.4f}", f"{x2:.4f}", str(label)])


def generate_algo_arrays(path: Path):
    payload = {
        "sorted_lists": [[1,2,3,5,7,9,12], [2,4,6,8,10]],
        "unsorted_lists": [[5,1,3,2,6,4], [10,9,8,7]],
        "windows": [[1,3,2,5,8,7,6], [4,2,12,3,6]],
    }
    with path.open("w") as f:
        json.dump(payload, f, indent=2)


if __name__ == "__main__":
    print(f"Generating datasets in {ROOT}")
    generate_students(ROOT / "students.csv")
    generate_regression(ROOT / "ml_regression.csv")
    generate_classification(ROOT / "ml_classification.csv")
    generate_algo_arrays(ROOT / "algo_arrays.json")
    print("Done. Files created: students.csv, ml_regression.csv, ml_classification.csv, algo_arrays.json")
