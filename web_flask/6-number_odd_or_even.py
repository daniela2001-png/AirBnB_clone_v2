#!/usr/bin/python3
"""
Comenzando con Flask!
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<string:text>", methods=["GET"], strict_slashes=False)
def cisfun(text):
    print("C {}".format(text.replace("_", " ")))


@app.route("/python", defaults={"text": "is cool"}, methods=["GET"],
           strict_slashes=False)
@app.route("/python/<string:text>", methods=["GET"], strict_slashes=False)
def python(text):
    return ("Python is {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", methods=["GET"], strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", methods=["GET"], strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", methods=["GET"],
           strict_slashes=False)
def even_odd(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
