#
from flask import Flask
__author__ = 'Monty Jones'

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

if __name__ == '__main__':
    pass
