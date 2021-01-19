#!/usr/bin/python3
"""
Comenzando con Flask!
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    return string
    """
    return "Hello HBNB!"


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbnb():
    """
    string
    """
    return "HBNB"


@app.route("/c/<string:text>", methods=["GET"], strict_slashes=False)
def cisfun(text):
    """
    str: true
    prop : true
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
