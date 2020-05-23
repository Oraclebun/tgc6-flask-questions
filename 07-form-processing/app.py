from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here!
@app.route("/")
def index():
    return render_template('index.template.html')

@app.route("/book")
def book():
	return render_template("book.template.html")

@app.route("/process_booking",methods=['POST'])
def display():
    #print(request.form)
    name = request.form.get('name')
    seating_type = request.form.get('seating-type')
    time = request.form.get('time')
    services = request.form.getlist('services')
    hear_about = request.form.get('how-did-you')
    return render_template("process_book.template.html", 
                            name=name,
                            seating_type = seating_type,
                            time=time,
                            services=", ".join(services),
                            hear_about=hear_about
                            )

if __name__ == '__main__':
    app.run(host=os.environ.get('127.0.0.1'),
            port=int(os.environ.get('PORT','8000')),
            debug=True)