#!/usr/bin/python3
"""
Comenzando con Flask!
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    a simple string to return
    """
    return "Hello HBNB!"


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbnb():
    """
    a simple string to return
    """
    return "HBNB"


@app.route("/c/<string:text>", methods=["GET"], strict_slashes=False)
def cisfun(text):
    """
    string without defautl values
    """
    print("C {}".format(text.replace("_", " ")))


@app.route("/python", defaults={"text": "is cool"}, methods=["GET"],
           strict_slashes=False)
@app.route("/python/<string:text>", methods=["GET"], strict_slashes=False)
def python(text):
    """
    python is (text)
    default value: python is cool
    """
    return ("Python is {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", methods=["GET"], strict_slashes=False)
def number(n):
    """
    is a  number or no ?
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", methods=["GET"], strict_slashes=False)
def number_template(n):
    """
    using jinja templates
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
