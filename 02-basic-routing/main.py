from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here
@app.route('/')
def home():
    return 'hi everybody'

@app.route('/about')
def about():
    return 'i am very smart'

@app.route('/double/<n>')
def double(n):
    return str(int(n)*2)

@app.route('/add/<int:n1>/<int:n2>')
def add_two(n1,n2):
    return str(n1+n2)

# "magic code" -- boilerplate
#if __name__ == '__main__':
#    app.run(host=os.environ.get('IP'),
#            port=int(os.environ.get('PORT')),
#            debug=True)

if __name__ == '__main__':
    app.run(host=os.environ.get('127.0.0.1'),
            port=int(os.environ.get('PORT','5000')),
            debug=True)