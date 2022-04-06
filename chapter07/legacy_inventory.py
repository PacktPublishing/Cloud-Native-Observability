#!/usr/bin/env python3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/inventory")
def inventory():
    products = [
        {"name": "oranges", "quantity": "10"},
        {"name": "apples", "quantity": "20"},
    ]
    return jsonify(products)


if __name__ == "__main__":
    app.run(port=5001)
