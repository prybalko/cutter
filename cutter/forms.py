from wtforms import StringField, validators
from flask_wtf import Form, FlaskForm


class UrlForm(FlaskForm):
    long_url = StringField('Url', [validators.Length(min=1, max=2100)])
