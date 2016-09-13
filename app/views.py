from flask import render_template, request
from app import app


@app.route("/")
def index():

    test = "hey i work sort of"

    return render_template("index.html", test=test)

