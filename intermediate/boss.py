"""Intermediate capstone: simple shopping application skeleton.

This module provides non-GUI building blocks for a shopping app:
- SQLite DB stored in `assets/workshop.db` for items and users
- Cart saved as JSON in `assets/cart_<userid>.json`
- Bills written to CSV in `assets/bills.csv`

Students: implement or integrate a Tkinter/CLI front-end that calls these
helpers. The database and files are under the `assets/` directory for easy
inspection and reset.
"""

from pathlib import Path
import csv
import json
from typing import Dict, Any, List

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)
DB_PATH = ASSETS / "workshop.db"
BILLS_CSV = ASSETS / "bills.csv"


# The SQL helper functions live in `intermediate/sql_handler.py`.
# Students should use those helper functions for DB operations.


def cart_path_for_user(user_id: str) -> Path:
    return ASSETS / f"cart_{user_id}.json"


def add_to_cart(user_id: str, item_id: int, qty: int = 1) -> Path:
    p = cart_path_for_user(user_id)
    cart: Dict[str, Any] = {"items": []}
    if p.exists():
        cart = json.loads(p.read_text(encoding="utf-8"))
    cart.setdefault("items", []).append({"item_id": item_id, "qty": qty})
    p.write_text(json.dumps(cart, indent=2), encoding="utf-8")
    return p


def view_cart(user_id: str) -> Dict[str, Any]:
    p = cart_path_for_user(user_id)
    if not p.exists():
        return {"items": []}
    return json.loads(p.read_text(encoding="utf-8"))


def checkout(user_id: str, user_info: Dict[str, Any]) -> Dict[str, Any]:
    """Perform a simple checkout: read cart, write a bill row in CSV, and clear cart.

    Returns a summary dict for confirmation.
    """
    cart = view_cart(user_id)
    # Students: implement price lookup, totals, taxes, and persist bill
    summary = {"user": user_id, "items": cart.get("items", []), "total": 0.0}
    # append to bills CSV
    header = ["user", "items", "total"]
    exists = BILLS_CSV.exists()
    with BILLS_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(header)
        writer.writerow([user_id, json.dumps(summary["items"]), f"{summary['total']:.2f}"])
    # clear cart
    p = cart_path_for_user(user_id)
    if p.exists():
        p.unlink()
    return summary


if __name__ == "__main__":
    print("Shopping app helpers ready. Implement UI (Tkinter or CLI) to use them.")