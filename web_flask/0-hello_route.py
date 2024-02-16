#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


# Define the route for the root URL.
@app.route("/", strict_slashes=False)
def hello():
    """Display 'Hello HBNB'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
