from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('127.0.0.1'),
            port=int(os.environ.get('PORT','8000')),
            debug=True)