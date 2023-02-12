#!/usr/bin/env python3
"""
a simple flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    outputs hello world
    """
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
