#!/usr/bin/python3
"""
Comenzando con Flask!
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    main page
    """
    return "Hello HBNB!"


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbnb():
    """
    return str
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
