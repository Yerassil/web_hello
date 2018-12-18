from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/bye')
def bye():
    return "Bye world!"


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        item = request.form['item']
        with open('db.txt', 'a') as f:
            f.write('\n' + item)
    with open('db.txt', 'r') as f:
        items = f.readlines()
    return render_template('hello.html', items=items)
