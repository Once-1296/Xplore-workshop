"""JSON file CRUD helpers (intermediate).

All JSON files live under `assets/`.
"""

from pathlib import Path
import json
from typing import Any

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def json_read(filename: str) -> Any:
    p = ASSETS / filename
    if not p.exists():
        raise FileNotFoundError(p)
    return json.loads(p.read_text(encoding="utf-8"))


def json_write(filename: str, payload: Any) -> Path:
    p = ASSETS / filename
    p.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return p


def json_update_key(filename: str, key_path: str, value: Any) -> bool:
    """Update a dotted key path (e.g. 'a.b.c') in the JSON and write back."""
    data = json_read(filename)
    keys = key_path.split('.') if key_path else []
    cur = data
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
    cur[keys[-1]] = value
    json_write(filename, data)
    return True


def json_delete_key(filename: str, key_path: str) -> bool:
    data = json_read(filename)
    keys = key_path.split('.') if key_path else []
    cur = data
    for k in keys[:-1]:
        cur = cur.get(k, {})
    if keys[-1] in cur:
        del cur[keys[-1]]
        json_write(filename, data)
        return True
    return False


if __name__ == "__main__":
    sample = {"a": {"b": 1}, "list": [1,2,3]}
    json_write("demo.json", sample)
    print(json_read("demo.json"))