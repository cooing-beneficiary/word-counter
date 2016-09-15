from collections import Counter
from flask import render_template, request
from app import app
from app.forms import WordForm

# Instantiate a Counter and return result of most_common 
def return_most_common(in_string):
    c = Counter(in_string)
    return c.most_common()[0][0]


# Route for index.html
@app.route("/", methods=["GET", "POST"])
def index():

    numchars = 0
    numwords = 0
    mostcommon_word = None
    mostcommon_char = None

    word_form = WordForm(request.form)

    if request.method == "POST" and len(word_form.user_input.data) > 0:

        # Get words, number of characters, and most common char and word.
        words = word_form.user_input.data
        numchars = len(words)
        numwords = len(words.split(' '))
        mostcommon_char = return_most_common(words)
        mostcommon_word = return_most_common(words.split())

    # Render the index view, passing our vars in our index.html.
    return render_template("index.html",
        word_form=word_form,
        numchars=numchars,
        numwords=numwords,
        mostcommon_word=mostcommon_word,
        mostcommon_char=mostcommon_char)
