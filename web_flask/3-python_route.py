#!/usr/bin/python3
"""
Comenzando con Flask!
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    return  a srting
    """
    return "Hello HBNB!"


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbnb():
    """
    return  a srting
    """
    return "HBNB"


@app.route("/c/<string:text>", methods=["GET"], strict_slashes=False)
def cisfun(text):
    """
    return  a srting
    using: prop
    """
    print("C {}".format(text.replace("_", " ")))


@app.route("/python", defaults={"text": "is cool"}, methods=["GET"],
           strict_slashes=False)
@app.route("/python/<string:text>", methods=["GET"], strict_slashes=False)
def python(text):
    """
    return  a srting
    using: prop
    """
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
