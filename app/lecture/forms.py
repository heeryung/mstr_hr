#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Quiz
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import User

# 다른 library를 쓸 때는 unicode - utf-8 의 문제인데 unicode로 다른 함수를 이용해 처리를 하고 나와 utf-8

class QuizForm(Form):
    qq0 = "이하는 객관식 및 단답형 주관식 문항입니다. 답을 잘 모르시겠는 경우 임의로 답을 선택하지 마시고 '잘 모르겠다'를 골라주세요."
    qa0 = "예"
    q0 = SelectField(str(qq0.encode('utf-8')), choiced=[(Y, qa0)], validators = [Required()])
    qq1 = "1. 다음 주어진 문장의 빈칸에 알맞는 단어를 연결한 보기를 고르시오. \"인간이 진화하면서 머리통은 (a)지고 얼굴이 (b)졌으며 씹는 기능은 (c)졌다.\""
    qa11 = "(a) 작아   (b)작아    (c) 약해"
    qa12 = "(a) 작아   (b)커      (c) 강해"
    qa13 = "(a) 커     (b)작아    (c) 약해"
    qa14 = "(a) 커     (b)커      (c) 강해" 
    qa15 = "(a) 작아   (b)커      (c) 약해"
    qa06 = "잘 모르겠다"
    q1 = SelectField(str(qq1.encode('utf-8')), choices=[('T', qa11), ('F', qa12), ('F2', qa13), ('F3', qa14), ('F4', qa15), ('K', qa06)], validators = [Required()])
    
    # 단답형으로 수정
    qq2 = "2. 뇌의 방향을 나타내기 위해 정의해야하는 것을 고르시오."
    qa21 = "영점, 한개의 면"
    qa22 = "영점, 두개의 면"
    qa23 = "영점, 세개의 면"
    qa24 = "영점, 네개의 면"
    qa25 = "영점, 다섯개의 면"
    q2 = SelectField(str(qq2.encode('utf-8')), choices=[('F1', qa21), ('F2', qa22), ('T', qa23), ('F3', qa24), ('F4', qa25), ('K', qa06) ], validators = [Required()]) 
    
    qq3 = '3. 위에 제시된 그림을 보고, 면(plane)의 명칭이 알맞은 순서로 나열된 것을 고르시오.'
    qa31 = "(a) coronal plane (b) horizontal plane (c) sagittal plane"
    qa32 = "(a) sagittal plane (b) coronal plane (c) orthogonal plane"
    qa33 = "(a) sagittal plane	(b) horizontal plane (c) orthogonal plane"
    qa34 = "(a) horizontal plane (b) sagittal plane	 (c) coronal plane"
    qa35 = "(a) coronal plane (b) sagittal plane (c) horizontal plane"
    q3 = SelectField(str(qq3.encode('utf-8')), choices = [('F1', qa31), ('F2', qa32), ('T', qa33), ('F3', qa34), ('F4', qa35), ('K', qa06) ], validators = [Required()]) 
    
    
    qq4 = 
    qa41 =
    qa42 = 
    qa43 =
    qa44 =
    qa45 =
    q4 = SelectField(str(qq4.encode('utf-8')), choices = [('F1', qa41), ('F2', qa42), ('T', qa43), ('F3', qa44), ('F4', qa45), ('K', qa06) ], validators = [Required()]) 
    
    
    qq5     
    # q4
    # q5
    # q6
    # q7
    # q8
    # q9
    # q10
    # q11
    # q12
    # q13
    # q14
    # q15
    # q16
    # q17
    # q18
    # q19
    q20 = StringField('What is the last name of the show host?', validators = [Required(), Length(1, 64)])