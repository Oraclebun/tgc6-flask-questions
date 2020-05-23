from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here!
@app.route("/")
def hello():
	return render_template("index.template.html")
	
@app.route("/",methods=['POST'])
def processHello():
    print(request.form)
    fn=request.form.get('first-name')
    ln=request.form.get('last-name')
    return render_template('process-hello.template.html', fn=fn, ln=ln)

@app.route("/calculate")
def getNumber():
    return render_template("process-calc.template.html")

@app.route("/calculate",methods=['POST'])
def processCalculate():
    print(request.form)
    number1 = request.form.get('number1')
    number2 = request.form.get('number2')
    result = str(int(number1)+int(number2))
    return render_template('display-calc.template.html', result=result)

# "magic code" -- boilerplate
#if __name__ == '__main__':
#    app.run(host=os.environ.get('IP'),
#            port=int(os.environ.get('PORT')),
#            debug=True)


if __name__ == '__main__':
    app.run(host=os.environ.get('127.0.0.1'),
            port=int(os.environ.get('PORT','8000')),
            debug=True)