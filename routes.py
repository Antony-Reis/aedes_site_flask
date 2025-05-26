from main import app
from flask import render_template

@app.route("/")
def render_home():
    return render_template("index.html")

@app.route("/validadorcpf")
def render_validarcpf():
    return render_template("validadorcpf.html")