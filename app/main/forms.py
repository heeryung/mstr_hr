from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask.ext.pagedown.fields import PageDownField
from ..models import Role, User

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class QuizForm(Form):
    answer = StringField('How can you answer?', validators=[Required()])
    submit = SubmitField('Submit')


class SummaryForm(Form):
    body = TextAreaField('How can you summary what you\'ve watched?', validators = [Required()])
    submit = SubmitField('Submit')
    
    
