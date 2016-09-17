import json
import requests
from collections import Counter
from flask import render_template, request
from app import app

# Our Feture Classes
from app.forms import WordForm
from app.forms import CalcForm

# Instantiate a Counter and return result of most_common 
def return_most_common(in_string):
    c = Counter(in_string)
    return c.most_common()[0][0]

# Simple calculator class.
class Calculator():
    def __init__(self):
        self.result = 0
        
    def add(self, n1, n2):
        return n1 + n2

    def sub(self,n1, n2):
        return n1 - n2

    def mult(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2


# Route for index.html
@app.route("/", methods=["GET", "POST"])
def index():

    numchars = 0
    numwords = 0
    mostcommon_word = None
    mostcommon_char = None

    word_form = WordForm(request.form)

    if request.method == "POST" and word_form.validate():

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

# Route for calculator.html
@app.route("/calc", methods=["GET", "POST"])
def calc():

    calc = Calculator()
    calc_form = CalcForm(request.form)
    result = 0

    if request.method == "POST" and calc_form.validate():
        print('calc called')
        n1 = calc_form.input1.data
        n2 = calc_form.input2.data
        op = calc_form.opers.data
        
        if op == 'ADD':
            result = calc.add(n1, n2)
        elif op == 'SUB':
            result = calc.sub(n1, n2)
        elif op == 'MULT':
            result = calc.mult(n1, n2)
        elif op == 'DIV':
            result = calc.div(n1, n2)


    return render_template("calc.html",
        calc_form=calc_form,
        result=result)



@app.route("/table", methods=["GET", "POST"])
def times_table():

    rows = []

    for row in range(1, 11):
        for col in range(1, 11):
            rows.append(row * col)


    return render_template("table.html", rows=rows)


# Route for random user data feature.

@app.route("/random_user", methods=["GET", "POST"])
def rand_user():

    def result_or_error(result):
        pass

    # Once user hits button.
    #if request.method == "POST":

    r = requests.get("https://randomuser.me/api?results=10")
    data = r.json()

    user_data = data["results"]
    return render_template("random_user.html", user_data=user_data)













