"""Web routing exercise (miscellaneous).

Create a minimal web app demonstrating CRUD-style routes.
Students may use Flask or FastAPI. This file provides an optional skeleton
that imports Flask only when needed so the module can still be imported
in environments without Flask installed.

Implement `create_app()` to return an app instance.
"""

from typing import Any


def create_app() -> Any:
    """Return a web app instance (Flask or FastAPI).

    If Flask is available, this function should create a Flask app with
    a few routes: GET /items, POST /items, GET /items/<id>, PUT /items/<id>, DELETE /items/<id>.
    If Flask is not installed, raise ImportError with a helpful message.
    """
    try:
        from flask import Flask, jsonify, request
    except Exception as e:
        raise ImportError("Flask is not available. Install it to run the web routing exercise.")

    app = Flask(__name__)

    # in-memory store for simple demonstration
    STORE = {"1": {"id": "1", "name": "sample"}}

    @app.route("/items", methods=["GET"])
    def list_items():
        return jsonify(list(STORE.values()))

    @app.route("/items", methods=["POST"])
    def create_item():
        payload = request.get_json() or {}
        new_id = str(len(STORE) + 1)
        item = {"id": new_id, **payload}
        STORE[new_id] = item
        return jsonify(item), 201

    @app.route("/items/<id>", methods=["GET"])
    def get_item(id):
        item = STORE.get(id)
        if not item:
            return ("Not Found", 404)
        return jsonify(item)

    @app.route("/items/<id>", methods=["PUT"])
    def update_item(id):
        if id not in STORE:
            return ("Not Found", 404)
        payload = request.get_json() or {}
        STORE[id].update(payload)
        return jsonify(STORE[id])

    @app.route("/items/<id>", methods=["DELETE"])
    def delete_item(id):
        if id in STORE:
            del STORE[id]
            return ("", 204)
        return ("Not Found", 404)

    return app


if __name__ == "__main__":
    try:
        app = create_app()
        app.run(port=5000)
    except ImportError as e:
        print(e)
        print("Install Flask to run this example: pip install flask")