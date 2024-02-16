#!/usr/bin/python3
""" module doc """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def doc """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ def doc """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
