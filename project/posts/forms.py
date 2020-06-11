from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    review = TextAreaField('Review', validators=[DataRequired()], render_kw={
                           'rows': 5})

    submit = SubmitField('Summarize')
