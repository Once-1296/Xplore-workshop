"""CSV file CRUD helpers (intermediate).

All CSV files are stored under `assets/`. Functions use the csv module and
operate on files inside the assets directory.
"""

from pathlib import Path
import csv
from typing import List, Dict, Any

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def csv_create(filename: str, headers: List[str], rows: List[List[Any]]) -> Path:
    p = ASSETS / filename
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    return p


def csv_read(filename: str) -> List[Dict[str, str]]:
    p = ASSETS / filename
    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def csv_append(filename: str, row: List[Any]) -> Path:
    p = ASSETS / filename
    with p.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)
    return p


def csv_update_row_by_index(filename: str, index: int, new_row: List[Any]) -> bool:
    p = ASSETS / filename
    rows = []
    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if index < 1 or index >= len(rows):
        # index 0 is headers
        return False
    rows[index] = new_row
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return True


def csv_delete(filename: str) -> bool:
    p = ASSETS / filename
    if p.exists():
        p.unlink()
        return True
    return False


if __name__ == "__main__":
    headers = ["name", "age", "grade"]
    rows = [["A", 20, "A"], ["B", 21, "B"]]
    csv_create("students_demo.csv", headers, rows)
    print(csv_read("students_demo.csv"))