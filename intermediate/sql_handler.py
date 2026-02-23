"""SQLite helper utilities (intermediate).

This module uses a sqlite database file under `assets/` so students can run
and inspect data easily. Keep SQL simple and safe from injections where possible.
"""

from pathlib import Path
import sqlite3
from typing import Any, List, Tuple

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)
DB_PATH = ASSETS / "workshop.db"


def get_conn():
    conn = sqlite3.connect(str(DB_PATH))
    return conn


def init_db(schema_sql: str = None):
    """Initialize the DB. If schema_sql is provided execute it, otherwise
    create a simple `items` table used by other exercises.
    """
    default_schema = """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL DEFAULT 0.0
    );
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.executescript(schema_sql or default_schema)
    conn.commit()
    conn.close()


def insert_item(name: str, price: float) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    rowid = cur.lastrowid
    conn.close()
    return rowid


def query_items() -> List[Tuple[int, str, float]]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM items ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_item(item_id: int, name: str = None, price: float = None) -> bool:
    conn = get_conn()
    cur = conn.cursor()
    updates = []
    params: List[Any] = []
    if name is not None:
        updates.append("name = ?")
        params.append(name)
    if price is not None:
        updates.append("price = ?")
        params.append(price)
    if not updates:
        conn.close()
        return False
    params.append(item_id)
    sql = f"UPDATE items SET {', '.join(updates)} WHERE id = ?"
    cur.execute(sql, params)
    conn.commit()
    conn.close()
    return True


def delete_item(item_id: int) -> bool:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = ?", (item_id,))
    affected = cur.rowcount
    conn.commit()
    conn.close()
    return affected > 0


if __name__ == "__main__":
    init_db()
    print("DB initialized at:", DB_PATH)
    print("Inserting sample item -> id", insert_item("Sample", 9.99))
    print("All items:", query_items())