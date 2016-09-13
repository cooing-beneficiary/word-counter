from wtforms import Form, StringField

class WeatherForm(Form):
    user_input = StringField("Enter a bunch of words")

    """
    def validate_words(form, field):
        if field.data == "assdf":
            raise ValidationError("Watcha doing Willis")

    """