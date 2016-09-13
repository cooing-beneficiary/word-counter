from wtforms import Form, StringField

class WordForm(Form):
    user_input = StringField("Enter a bunch of words")
