#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
    q = "오늘 시청한 강의를 다섯문장 이상으로 요약해주세요."
    body = TextAreaField(str(q.encode('utf-8')), validators = [Required()])
    submit = SubmitField('Submit')
    print "=================="
    print "called-000"
    print "=================="
    
    
