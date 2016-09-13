from flask import render_template, request
from app import app
from app.forms import WordForm

@app.route("/", methods=["GET", "POST"])
def index():
    word_form = WordForm(request.form)

    # The words the user input.
    
    words = word_form.user_input.data

    # The number of characters in input.
    numchars = len(words)

    # The number of words in user input.
    numwords = len(words.split(' '))
    mostcommon = 'not done'

    return render_template("index.html", word_form=word_form, numchars=numchars, numwords=numwords, mostcommon=mostcommon)
