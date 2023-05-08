from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/capabilities")
def capabilities():
    return render_template("capabilities.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

