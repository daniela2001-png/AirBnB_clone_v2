#!/usr/bin/python3
"""
Comenzando con Flask!
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    main index page
    """
    return "Hello HBNB!"


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbnb():
    """
    return string
    """
    return "HBNB"


@app.route("/c/<string:text>", methods=["GET"], strict_slashes=False)
def cisfun(text):
    """
    using props
    string : true
    """
    print("C {}".format(text.replace("_", " ")))


@app.route("/python", defaults={"text": "is cool"}, methods=["GET"],
           strict_slashes=False)
@app.route("/python/<string:text>", methods=["GET"], strict_slashes=False)
def python(text):
    """
    props and default values
    """
    return ("Python is {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", methods=["GET"], strict_slashes=False)
def number(n):
    """
    is a number ? or no
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
