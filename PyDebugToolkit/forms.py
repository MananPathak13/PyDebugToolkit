from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProcessForm(FlaskForm):
    process_name = StringField('Process Name', validators=[DataRequired()])
    submit = SubmitField('Monitor')
