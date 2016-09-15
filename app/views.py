from collections import Counter
from flask import render_template, request
from app import app
from app.forms import WordForm


def return_most_common(in_string):
    c = Counter(in_string)
    return c.most_common()[0][0]



@app.route("/", methods=["GET", "POST"])
def index():

    numchars = 0
    numwords = 0
    mostcommon_word = None
    mostcommon_char = None

    word_form = WordForm(request.form)

    if request.method == "POST" and len(word_form.user_input.data) > 0:

        # The words the user input.
        words = word_form.user_input.data

        # The number of characters in input.
        numchars = len(words)

        # The number of words in input.
        numwords = len(words.split(' '))

        # The most common character.
        mostcommon_char = return_most_common(words)
        
        # The most common word.
        mostcommon_word = return_most_common(words.split())

    # Render the index view, passing our vars displayed in our index.html view.
    return render_template("index.html",
        word_form=word_form,
        numchars=numchars,
        numwords=numwords,
        mostcommon_word=mostcommon_word,
        mostcommon_char=mostcommon_char)




