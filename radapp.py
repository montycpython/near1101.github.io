#!/usr/bin/python
__author__ = 'Montavious'
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "4d1ce3e001c8bc4932be3c57d12b8205ad75f38b493a24026d7abf067af3c146"

@app.route("/")
@app.route("/<name>")
def hello_world(name=None):
    "Should serve as the cover of a book or a book store front."
    return render_template("index.html", name=name)
    # request, session, g, and get_flashed_messages() are available in every jinja2 template for Flask

@app.route("/signin", methods=["GET","POST"])
def log_in():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'secret':
            error = 'Invalid credentials!'
            flash(error)
        else:
            flash('You were successfully logged in!')
            return redirect(url_for('hello_world', name=request.form["username"].title()))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
