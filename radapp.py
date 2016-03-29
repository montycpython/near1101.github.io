#!/usr/bin/python
__author__ = 'Montavious'
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello!!!!! &#x2766;</h1>"

if __name__ == '__main__':
    app.run()
