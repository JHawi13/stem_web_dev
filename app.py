from flask import Flask
from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template("Portfolio_homepage/Portfolio.html")
@app.route('/contact/')
def contact_page():
    return render_template("Portfolio_homepage/Forms/contact_form.html")
