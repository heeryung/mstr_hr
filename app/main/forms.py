from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.pagedown.fields import PageDownField

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class Quizanswer(Form):
    answer = StringField('How can you answer?', validators=[Required()])
    submit = SubmitField('Sumbmit')


class SummaryForm(Form):
    body = PageDownField('How can you summary what you\'ve watched?', validators = [Required()])
    submit = SubmitField('Submit')
    
    
