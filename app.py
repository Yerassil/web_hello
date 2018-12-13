from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/bye')
def bye():
    return "Bye world!"


@app.route('/')
def hola():
    return render_template('hello.html')
