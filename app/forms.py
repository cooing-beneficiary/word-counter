from wtforms import Form, StringField, IntegerField, RadioField

class WordForm(Form):
    user_input = StringField("Enter a bunch of words")


class CalcForm(Form):
	input1 = IntegerField("N1")
	input2 = IntegerField("N2")
	opers = RadioField("Operators",
        default='+',
        choices = [
            ('ADD', '+'),
            ('SUB', '-'),
            ('MULT', '*'),
            ('DIV', '/')
        ])
