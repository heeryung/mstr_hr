#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask.ext.pagedown.fields import PageDownField
from ..models import Role, User

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')



class SummaryForm(Form):
    q = "오늘 시청한 강의를 다섯문장 이상으로 요약해주세요. &#13;&#10; 작성 후 반드시 아래의 \"Save\" 버튼을 눌러 글을 저장하신 후에 \"Next\"를 눌러주세요."
    body = TextAreaField(str(q.encode('utf-8')), validators = [Required()])
    submit = SubmitField('Save')
    


class PreSurveyForm(Form) :
    rq_int = "시청하시게 될 강의는 서울대학교에서 제공하는 기독교 개론 강의입니다. 해당 강의의 주제에 대해 평소 얼마나 \'관심\'이 있으셨습니까?"
    r1_int = "전혀 관심이 없다"
    r2_int = "관심이 없는 편이다"
    r3_int = "관심이 있는 편이다"
    r4_int = "매우 관심이 있다"
    r_int = RadioField(str(rq_int.encode('utf-8')), choices = [('1', r1_int), ('2', r2_int), ('3', r3_int), ('4', r4_int)], validators = [Required()])
    
    rq_know = "시청하시게 될 강의의 주제인 기독교 개론에 대해 평소 얼마나 \'알고\' 계셨습니까?"
    r1_know = "전혀 알지 못한다"
    r2_know = "거의 알지 못한다"
    r3_know = "어느 정도 알고 있다"
    r4_know = "매우 잘 알고 있다"
    r_know = RadioField(str(rq_know.encode('utf-8')), choices = [('1', r1_know), ('2', r2_know), ('3', r3_know), ('4', r4_know)], validators = [Required()])
    
    submit = SubmitField('Submit')
    
#
# class BrainForm(Form):
#     qq0 = "이하는 객관식 및 단답형 주관식 문항입니다. 답을 잘 모르시겠는 경우 임의로 답을 선택하지 마시고 '잘 모르겠다'를 골라주세요."
#     qa0 = "예"
#     q0 = RadioField(str(qq0.encode('utf-8')), choices=[('Y', qa0)], validators = [Required()])
#
#
#     qq1 = "1. 다음 주어진 문장의 빈칸에 알맞는 단어를 연결한 보기를 고르시오. \"인간이 진화하면서 머리통은 (a)지고 얼굴이 (b)졌으며 씹는 기능은 (c)졌다.\""
#     qa11 = "(a) 작아   (b)작아    (c) 약해"
#     qa12 = "(a) 작아   (b)커      (c) 강해"
#     qa13 = "(a) 커     (b)작아    (c) 약해"
#     qa14 = "(a) 커     (b)커      (c) 강해"
#     qa15 = "(a) 작아   (b)커      (c) 약해"
#     qa06 = "잘 모르겠다"
#     q1 = RadioField(str(qq1.encode('utf-8')), choices=[('T', qa11), ('F', qa12), ('F2', qa13), ('F3', qa14), ('F4', qa15), ('K', qa06)], validators = [Required()])
#
#     # (youngjum, 3myun)
#     qq2 = "2. 뇌의 방향을 나타내기 위해 정의해야하는 두 가지를 적으시오. (예: A, B)"
#     q2 = StringField('Code', validators = [Required(), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
#                                           qq2.encode('utf-8'))])
#
#
#
#
#     qq3 = '3. 위에 제시된 그림을 보고, 면(plane)의 명칭이 알맞은 순서로 나열된 것을 고르시오.'
#     qa31 = "(a) coronal plane (b) horizontal plane (c) sagittal plane"
#     qa32 = "(a) sagittal plane (b) coronal plane (c) orthogonal plane"
#     qa33 = "(a) sagittal plane    (b) horizontal plane (c) orthogonal plane"
#     qa34 = "(a) horizontal plane (b) sagittal plane     (c) coronal plane"
#     qa35 = "(a) coronal plane (b) sagittal plane (c) horizontal plane"
#     q3 = RadioField(str(qq3.encode('utf-8')), choices = [('F1', qa31), ('F2', qa32), ('T', qa33), ('F3', qa34), ('F4', qa35), ('K', qa06) ], validators = [Required()])
#
#
#     # 답
#     qq4 = '[]의 글을 읽고, 사람을 기준으로 할 때 뇌의 방향과 관련해 제시된 빈칸을 알맞게 채운 것을 고르시오. [(a) = anterior (b) = posterior]'
#     qa41 = '(a) ventral (b) dorsal'
#     qa42 = '(a) rostral (b) caudal'
#     qa43 = '(a) ventral (b) caudal'
#     qa44 = '(a) rostral (b) ventral'
#     qa45 = '(a) rostral (b) dorsal'
#     q4 = RadioField(str(qq4.encode('utf-8')), choices = [('F1', qa41), ('F2', qa42), ('T', qa43), ('F3', qa44), ('F4', qa45), ('K', qa06) ], validators = [Required()])
#
#
#     #답
#     qq5 = '다음 중 강의에서 뇌의 중추신경계의 구조로 언급되지 않은 것을 고르시오.'
#     qa51 = '대뇌 (cerebrum)'
#     qa52 = '뇌엽 (Lobes of the brain)'
#     qa53 = '뇌간 (brain storm)'
#     qa54 = '척수 (spinal cord)'
#     qa55 = '소뇌 (cerebellum)'
#     q5 = RadioField(str(qq5.encode('utf-8')), choices = [('F1', qa51), ('F2', qa52), ('T', qa53), ('F3', qa54), ('F4', qa55), ('K', qa06) ], validators = [Required()])
#
#
#     qq6 = ''
#     qa61 = ''
#     qa62 = ''
#     # q4
#     # q5
#     # q6
#     # q7
#     # q8
#     # q9
#     # q10
#     # q11
#     # q12
#     # q13
#     # q14
#     # q15
#     # q16
#     # q17
#     # q18
#     # q19
#     q20 = StringField('What is the last name of the show host?', validators = [Required(), Length(1, 64)])
#
#     submit = SubmitField('Submit')
    

class ReligionForm(Form):
    rqq0 = "이하는 객관식 및 단답형 주관식 문항입니다. 답을 잘 모르시겠는 경우 임의로 답을 선택하지 마시고 '잘 모르겠다'를 골라주세요."
    rqa0 = "예"
    rq0 = RadioField(str(rqq0.encode('utf-8')), choices=[("Y", rqa0)], validators = [Required()])




    rqq1 = "다음 중 강의에서 설명한 \'천국\'과 가장 관련이 없는 것을 고르시오."
    rqa11 = "Kingdom of God"
    rqa12 = "Kingdom of heavens"
    rqa13 = "바실레이아"
    rqa14 = "regnum" 
    rqa15 = "사후세계"
    rqa06 = "잘 모르겠다"
    rq1 = RadioField(str(rqq1.encode('utf-8')), choices=[('F4', rqa11), ('F1', rqa12), ('F2', rqa13), ('F3', rqa14), ('T', rqa15), ('K', rqa06)], validators = [Required()])
    

    rqq2 = '아래 [   ]안의 글을 읽고 (a)에 들어갈 말로 알맞은 말을 적으시오. (답을 모를 경우 \'잘 모르겠다\'고 적어주십시오.)'
    rq2 = TextAreaField(str(rqq2.encode('utf-8')), validators=[Required()])
    



    rqq15 = "다음 문장에서 아래 [   ]의 (a)에 들어갈 말로 알맞은 것을 적으시오. (답을 모를 경우 \'잘 모르겠다\'고 적어주십시오.)" 
    rq15 = TextAreaField(str(rqq15.encode('utf-8')), validators=[Required()])
    
    
 
    
    rqq4 = '강의 내용에 기반할 때 다음 중 \'회개\'에 대한 설명으로 틀린 것은 무엇인가?'
    rqa41 = "잘못을 돌아보는 것이다."
    rqa42 = "내 삶을 새롭게 정의하는 것이다."
    rqa43 = "자신의 마음을 들여다보는 것이다."
    rqa44 = "히브리어로 회복을 의미한다."
    rqa45 = "신의 형상을 한 인간이 본래의 마음을 되찾고자 하는 것이다."
    rq4 = RadioField(str(rqq4.encode('utf-8')), choices = [('T', rqa41), ('F2', rqa42), ('F1', rqa43), ('F3', rqa44), ('F4', rqa45), ('K', rqa06) ], validators = [Required()]) 
        
    
    
    rqq3 = '다음 중 혼자 다른 인물에 대한 이야기를 하고 있는 사람을 고르시오.'
    rqa31 = "A: 이 인물은 그리스도교를 팔레스타인 너머로 확장하는데 기여했다."
    rqa32 = "B: 이 인물은 유대인이었으며 랍비였다."
    rqa33 = "C: 이 인물은 당대 그리스 로마 교육의 중심지인 터키 출신이었다."
    rqa34 = "D: 이 인물은 예수에게 세례를 주었다."
    rqa35 = "E: 이 인물은 최초의 신약성서와 관련이 있다."
    rq3 = RadioField(str(rqq3.encode('utf-8')), choices = [( "F", rqa31), ("F", rqa32), ("F", rqa33), ("T", rqa34), ("F", rqa35), ('K', rqa06) ], validators = [Required()])    
    
    #답?
    rqq6 = '강의 내용에 기반할 때, 일반적으로 사탄(Satan)에게 유혹을 받을 가능성이 가장 \'낮은\' 상황을 고르시오.'
    rqa61 = "A는 축복의 땅에서 아무런 고통없이 살고 있다."
    rqa62 = "B는 과거 위대한 왕이었으나 말년에 과한 세금을 부과하였고 나이가 들어 쇠약해졌다."
    rqa63 = "C는 신에 대한 충성심이 높기로 일대에서 유명했다."
    rqa64 = "D는 남다른 외모의 소유자였으며 형을 속여 장자로서의 권리를 양도받을 정도로 영리했다."
    rqa65 = "E는 신의 사랑을 받고 거처를 옮긴 뒤 100세에 처음 자식을 얻었다."
    rq6 = RadioField(str(rqq6.encode('utf-8')), choices = [('T', rqa61), ('F2', rqa62), ('F1', rqa63), ('F3', rqa64), ('F4', rqa65), ('K', rqa06) ], validators = [Required()])
    


    rqq7 = '강의에 기반할 때 다음 중 성서에 등장한 물의 메타포와 가장 거리가 먼 것을 고르시오.'
    rqa71 = "요단강"
    rqa72 = "스틱스강"
    rqa73 = "사막에서의 방황"
    rqa74 = "홍해"
    rqa75 = "모두 성서에서의 물의 메타포와 관련이 있다"
    rq7 = RadioField(str(rqq7.encode('utf-8')), choices = [("F1", rqa71 ), ("F2", rqa72), ("F", rqa73), ("F", rqa74), ("T", rqa75), ("K", rqa06) ], validators = [Required()])
    
    
    rqq8 = '아래 [   ]안의 글은 성경 구절의 일부를 수정한 것이다. 강의내용에 기반할 때 제시된 구절과 관련하여 가장 거리가 먼 추측을 한 사람을 고르시오.'
    rqa81 = "A: 사탄은 신의 아들인가보네."
    rqa82 = "B: 욥은 하나님의 사랑을 받지 않았을까?"
    rqa83 = "C: 사탄은 하나님의 뜻에 따라서 욥을 시험했겠군."
    rqa84 = "D: 욥은 아마 유혹에 빠지지 쉬운 나약한 인물이었을거야."
    rqa85 = "E: 욥은 사탄의 예상과는 달리 하나님을 원망하지 않았을거야."
    rq8 = RadioField(str(rqq8.encode('utf-8')), choices = [( 'F1', rqa81), ("T", rqa82), ("F2", rqa83), ("F3", rqa84), ("F4", rqa85), ( 'K', rqa06) ], validators = [Required()])
    
    
    rqq9 = '다음은 예수가 세례를 받던 순간에 대한 묘사이다. 강의내용에 기반할 때 이와 관련해 잘못된 것을 고르시오.'
    rqa91 = "A: 세례를 주는 사람이 예수를 치켜세웠다."
    rqa92 = "B: 예수에게 세례를 주는 사람이 세례 요한이구나."
    rqa93 = "C: 고통에 빠져있던 예수는 세례로 평안을 얻었다."
    rqa94 = "D: 예수가 세례를 받을 때 비둘기 같은 성령이 모여들었다."
    rqa95 = "E: 예수에게 세례를 준 사람은 예수보다 먼저 나타나 예수가 올 것을 예비한 존재이다."
    rq9 = RadioField(str(rqq9.encode('utf-8')), choices = [( 'F1', rqa91), ( 'F2', rqa92), ( "T", rqa93), ("F3", rqa94), ("F4", rqa95), ("K", rqa06) ], validators = [Required()])
    
    

    rqq10 = "아래 [   ]에서 설명하는 인물의 이름을 적으시오.  "
    rq10 =  TextAreaField(str(rqq10.encode('utf-8')), validators=[Required()])

    
    #답
    rqq11 = '강의 내용에 기반할 때 다음 중 틀린 설명을 고르시오.'
    rqa111 = "A: 존 밀튼은 그리스도가 사탄의 시험을 받는 것과 관련된 문학작품을 쓴 바 있다."
    rqa112 = "B: 예수가 이겨낸 첫번째 유혹은 물질 유혹이었다."
    rqa113 = "C: \'사탄\'이라는 명칭에는 신에게 고발하는 자라는 뜻이 있다."
    rqa114 = "D: 제 2의 아담이라는 별칭에는 또 다시 죄를 지을 자라는 의미가 있다."
    rqa115 = "E: 말커싸(말쿠쓰)에는 신의 뜻이 이뤄지는 곳, 상태라는 의미가 있다."
    rq11 = RadioField(str(rqq11.encode('utf-8')), choices = [("F1", rqa111), ("F2", rqa112), ("F3", rqa113), ("T", rqa114), ("F", rqa115), ("K", rqa06) ], validators = [Required()])




    rqq12 = '위의 이미지를 보고 이와 관련해 다음 중 맞는 설명을 고르시오.'
    rqa121 = "랍비에 의해 발견되었다."
    rqa122 = "현재까지 발견된 가장 오래된 성서가 발견된 곳이다."
    rqa123 = "히브리어로 적혀져 있는 문서가 발견되었다."
    rqa124 = "지금은 소실되었다"
    rqa125 = "레닌그라드 코덱스라고도 한다."
    rq12 = RadioField(str(rqq12.encode('utf-8')), choices = [('F1', rqa121), ('F2', rqa122), ('T', rqa123), ('F3', rqa124), ('F4', rqa125), ('K', rqa06) ], validators = [Required()])




    rqq13 = "강의 내용에 기반할 때 다음 중 맞는 설명을 고르시오."
    rqa131 = "예수를 시험한 주체는 하나님이자 성령이다."
    rqa132 = "예수의 명칭 중 하나는 인간의 아들로 인간 어머니의 몸을 빌어 태어났음을 말한다."
    rqa133 = "이사야는 \'저는 물로 세례를 주었지만 뒤이어 오실 이(예수)는 성령으로 세례를 주실 것입니다\'라고 말했다"
    rqa134 = "세례, 성수, 홍해의 공통점은 영혼의 정화라는 의미가 있다는 것이다"
    rqa135 = "예수는 세례를 통해 영적 충만함을 이룩했고 그를 통해 지상에서의 자신의 임무를 완수했다."
    rq13 = RadioField(str(rqq13.encode('utf-8')), choices = [('T', rqa131), ('F2', rqa132), ('T', rqa133), ('F3', rqa134), ('F4', rqa135), ('K', rqa06) ], validators = [Required()])
    
    
    
    
    rqq14 = '강의 내용에 기반할 때 다음 중 광야에서 예수가 받은 사탄의 유혹 내용이 바르게 짝지어진 것을 고르시오.'  
    rqa141 = "권력욕 - 세상의 모든 영광을 보아라. 네가 나에게 엎드려 절하면 이를 모두 줄 것이다."
    rqa142 = "권력욕 - 네가 하나님의 아들이거든 돌을 빵이 되라고 말해보아라."
    rqa143 = "물질유혹 - 네가 뛰어내리면 천사들이 너의 발을 받쳐줄 것이다." 
    rqa144 = "영적유혹 -  세상의 모든 영광을 보아라. 네가 나에게 엎드려 절하면 이를 모두 줄 것이다."
    rqa145 = "영적유혹 - 네가 뛰어내리면 천사들이 너의 발을 받쳐줄 것이다."
    rq14 = RadioField(str(rqq14.encode('utf-8')), choices = [("F1", rqa141), ('F2', rqa142), ("F3", rqa143), ("T", rqa144), ('F4', rqa145), ('K', rqa06) ], validators = [Required()])




    rqq5 = '강의 내용에 기반할 때 다음 중 광야에서 예수가 유혹을 뿌리친 것의 의미를 바르게 짝지어진 것을 고르시오.'
    rqa51 = "권력욕 - 자신의 욕망이 아니라 신이 말씀하시는 내용을 따라야한다."
    rqa52 = "권력욕 - 사람은 하나님의 입에서 나오는 모든 말씀으로 살 것이다." 
    rqa53 = "물질유혹 - 자신의 욕망이 아니라 신이 말씀하시는 내용을 따라야한다."
    rqa54 = "영적유혹 - 사람은 하나님의 입에서 나오는 모든 말씀으로 살 것이다." 
    rqa55 = "영적유혹 - 주 너의 하나님을 시험하지 말라."
    rq5 = RadioField(str(rqq5.encode('utf-8')), choices = [("F1", rqa51), ("F3", rqa52), ("F2", rqa53), ('T', rqa54), ('F4', rqa55), (  'K', rqa06) ], validators = [Required()])



    submit = SubmitField('Submit')
    
    
class PostSurvey_AForm(Form):
    q_helpful = "이 강의는 교육적인 면에서 볼 때 \'도움이 된다.\' (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"    
    helpful_a = RadioField(str(q_helpful.encode('utf-8')),
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')],
        validators=[Required()], default=None)
    
    q_useful = "이 강의는 교육적인 면에서 볼 때 \'유용하다.\' (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"     
    useful_a = RadioField(str(q_useful.encode('utf-8')),
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')],
        validators=[Required()], default=None)
    
    q_curious = "이 강의는 교육적인 면에서 볼 때 \'더 배우고 싶다는 호기심을 불러일으킨다.\' (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"       
    curious_a = RadioField(str(q_curious.encode('utf-8')),
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')],
        validators=[Required()], default=None)
        
    q_satisfy = "이 강의는 \'불만족스러웠다\'. (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"    
    satisfy_a = RadioField(str(q_satisfy.encode('utf-8')),
        choices=[('7', '1'), ('6', '2'), ('5', '3'), ('4', '4'), ('3', '5'), ('2', '6'), ('1', '7')],
        validators=[Required()], default=None)
    
    q_annoy = "이 강의는 나를 \'짜증나게\' 했다. (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"    
    annoy_a = RadioField(str(q_annoy.encode('utf-8')),
        choices=[('7', '1'), ('6', '2'), ('5', '3'), ('4', '4'), ('3', '5'), ('2', '6'), ('1', '7')],
        validators=[Required()], default=None)
    
    q_frustrated = "이 강의는 나를 \'혼란스럽게\' 했다. (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"    
    frustrated_a = RadioField(str(q_frustrated.encode('utf-8')),
        choices=[('7', '1'), ('6', '2'), ('5', '3'), ('4', '4'), ('3', '5'), ('2', '6'), ('1', '7')],
        validators=[Required()], default=None)
        
    submit = SubmitField('Submit')


class PostSurvey_BForm(Form): 
    q_helpful = "이 강의는 교육적인 면에서 볼 때 \'도움이 된다.\' (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"
    helpful_b = RadioField(str(q_helpful.encode('utf-8')),
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')],
        validators=[Required()], default=None)
    
    q_useful = "이 강의는 교육적인 면에서 볼 때 \'유용하다.\' (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"    
    useful_b = RadioField(str(q_useful.encode('utf-8')),
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')],
        validators=[Required()], default=None)
    
    q_curious = "이 강의는 교육적인 면에서 볼 때 \'더 배우고 싶다는 호기심을 불러일으킨다.\' (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"    
    curious_b = RadioField(str(q_curious.encode('utf-8')),
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')],
        validators=[Required()], default=None)
        
    q_satisfy = "이 강의는 \'불만족스러웠다\'. (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"
    satisfy_b = RadioField(str(q_satisfy.encode('utf-8')),
        choices=[('7', '1'), ('6', '2'), ('5', '3'), ('4', '4'), ('3', '5'), ('2', '6'), ('1', '7')],
        validators=[Required()], default=None)
    
    q_annoy = "이 강의는 나를 \'짜증나게\' 했다. (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"
    annoy_b = RadioField(str(q_annoy.encode('utf-8')),
        choices=[('7', '1'), ('6', '2'), ('5', '3'), ('4', '4'), ('3', '5'), ('2', '6'), ('1', '7')],
        validators=[Required()], default=None)
    
    q_frustrated = "이 강의는 나를 \'혼란스럽게\' 했다. (전혀 그렇지 않다:1, 보통이다:4, 매우 그렇다:7)"
    frustrated_b = RadioField(str(q_frustrated.encode('utf-8')),
        choices=[('7', '1'), ('6', '2'), ('5', '3'), ('4', '4'), ('3', '5'), ('2', '6'), ('1', '7')],
        validators=[Required()], default=None)
    
    q_gender = "성별을 표기해주십시오. (e.g. 남성, 여성, 그 외)"
    q1_gender = "남성"
    q2_gender = "여성"
    q3_gender = "그 외"
    gender = RadioField(q_gender,
        choices=[('M', q1_gender), ('F', q2_gender), ('O', q3_gender)],
        validators=[Required()], default=None)

    q_age = "나이를 표기해주십시오. 만 나이로 적어주시기 바랍니다. (예: 29)"    
    age = TextAreaField(q_age, validators=[Required()])

    
