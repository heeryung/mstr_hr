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

class QuizForm_B(Form):
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
    
    
    # 답
    qq4 = '[]의 글을 읽고, 사람을 기준으로 할 때 뇌의 방향과 관련해 제시된 빈칸을 알맞게 채운 것을 고르시오. [(a) = anterior (b) = posterior]'
    qa41 = '(a) ventral (b) dorsal'
    qa42 = '(a) rostral (b) caudal'
    qa43 = '(a) ventral (b) caudal'
    qa44 = '(a) rostral (b) ventral'
    qa45 = '(a) rostral (b) dorsal'
    q4 = SelectField(str(qq4.encode('utf-8')), choices = [('F1', qa41), ('F2', qa42), ('T', qa43), ('F3', qa44), ('F4', qa45), ('K', qa06) ], validators = [Required()]) 
    
    
    #답
    qq5 = '다음 중 강의에서 뇌의 중추신경계의 구조로 언급되지 않은 것을 고르시오.'
    qa51 = '대뇌 (cerebrum)' 
    qa52 = '뇌엽 (Lobes of the brain)'
    qa53 = '뇌간 (brain storm)'
    qa54 = '척수 (spinal cord)'
    qa55 = '소뇌 (cerebellum)'    
    q5 = SelectField(str(qq5.encode('utf-8')), choices = [('F1', qa51), ('F2', qa52), ('T', qa53), ('F3', qa54), ('F4', qa55), ('K', qa06) ], validators = [Required()]) 
    
    
    qq6 = ''
    qa61 = ''
    qa62 = ''
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
    
    
    

class QuizForm_R(Form):
    qq0 = "이하는 객관식 및 단답형 주관식 문항입니다. 답을 잘 모르시겠는 경우 임의로 답을 선택하지 마시고 '잘 모르겠다'를 골라주세요."
    qa0 = "예"
    q0 = SelectField(str(qq0.encode('utf-8')), choiced=[(Y, qa0)], validators = [Required()])
    qq1 = "1. 다음 중 강의에서 설명한 \'천국\'과 가장 관련이 없는 것을 고르시오."
    qa11 = "Kingdom of God"
    qa12 = "Kingdom of heavens"
    qa13 = "바실레이아"
    qa14 = "regnum" 
    qa15 = "사후세계"
    qa06 = "잘 모르겠다"
    q1 = SelectField(str(qq1.encode('utf-8')), choices=[('F4', qa11), ('F1', qa12), ('F2', qa13), ('F3', qa14), ('T', qa15), ('K', qa06)], validators = [Required()])
    
    
    #단답형으로 수정 / 답 체크
    qq2 = "2. 다음 문장에서 (a)들어갈 말로 알맞은 것을 적으시오."
    qa21 = "회개"
    qa22 = "쿰란"
    qa23 = "세례"
    qa24 = "천국"
    qa25 = "재래"
    q2 = SelectField(str(qq2.encode('utf-8')), choices=[('F1', qa21), ('F2', qa22), ('T', qa23), ('F3', qa24), ('F4', qa25), ('K', qa06) ], validators = [Required()])
    
    
    #단답형으로 수정. 답 체크    
    qq3 = '3. 다음 []안의 글을 읽고 (a)에 들어갈 말로 알맞은 말을 적으시오. (답을 모를 경우 \'잘 모르겠다\'고 적어주십시오.) \[(a)는(은) 로마 제국에서 사면을 할 때 주는 편지에서 지칭하는 말에서 유래되었다. (a)에 대한 믿음 없이는 구원도 없다는 점 때문에 (a)(이)라는 명칭으로 신약성서에 언급되었다.\]'
    qa31 = "(a) coronal plane (b) horizontal plane (c) sagittal plane"
    qa32 = "(a) sagittal plane (b) coronal plane (c) orthogonal plane"
    qa33 = "(a) sagittal plane	(b) horizontal plane (c) orthogonal plane"
    qa34 = "(a) horizontal plane (b) sagittal plane	 (c) coronal plane"
    qa35 = "(a) coronal plane (b) sagittal plane (c) horizontal plane"
    q3 = SelectField(str(qq3.encode('utf-8')), choices = [('F1', qa31), ('F2', qa32), ('T', qa33), ('F3', qa34), ('F4', qa35), ('K', qa06) ], validators = [Required()]) 
    
    
    qq4 = '강의 내용에 기반할 때 다음 중 \'회개\'에 대한 설명으로 틀린 것은 무엇인가?'
    qa41 = "잘못을 돌아보는 것이다."
    qa42 = "내 삶을 새롭게 정의하는 것이다."
    qa43 = "자신의 마음을 들여다보는 것이다."
    qa44 = "히브리어로 회복을 의미한다."
    qa45 = "신의 형상을 한 인간이 본래의 마음을 되찾고자 하는 것이다."
    q4 = SelectField(str(qq4.encode('utf-8')), choices = [('T', qa41), ('F2', qa42), ('F1', qa43), ('F3', qa44), ('F4', qa45), ('K', qa06) ], validators = [Required()]) 
        
    
    #답?    
    qq5 = '다음 중 혼자 다른 인물에 대한 이야기를 하고 있는 사람을 고르시오.'
    qa51 = "A\: 이 인물은 그리스도교를 팔레스타인 너머로 확장하는데 기여했다."
    qa52 = "B\: 이 인물은 유대인이었으며 랍비였다."
    qa53 = "C\: 이 인물은 당대 그리스 로마 교육의 중심지인 터키 출신이었다."
    qa54 = "D\: 이 인물은 예수에게 세례를 주었다."
    qa55 = "E\: 이 인물은 최초의 신약성서와 관련이 있다."
    q5 = SelectField(str(qq5.encode('utf-8')), choices = [('T', qa51), ('F2', qa52), ('F1', qa53), ('F3', qa54), ('F4', qa55), ('K', qa06) ], validators = [Required()])    
    
    #답?
    qq6 = '강의 내용에 기반할 때, 일반적으로 사탄(Satan)에게 유혹을 받을 가능성이 가장 \'낮은\' 상황을 고르시오.'
    qa61 = "A는 축복의 땅에서 아무런 고통없이 살고 있다."
    qa62 = "B는 과거 위대한 왕이었으나 말년에 과한 세금을 부과하였고 나이가 들어 쇠약해졌다."
    qa63 = "C는 신에 대한 충성심이 높기로 일대에서 유명했다."
    qa64 = "D는 남다른 외모와 키를 가지고 있었고, 형을 속여 장자로서의 권리를 양도받을 정도로 영리했다."
    qa65 = "E는 신의 사랑을 받고 거처를 옮긴 뒤 100세에 처음 자식을 얻었다."
    q6 = SelectField(str(qq6.encode('utf-8')), choices = [('T', qa61), ('F2', qa62), ('F1', qa63), ('F3', qa64), ('F4', qa65), ('K', qa06) ], validators = [Required()])
    
    
    #답?
    qq7 = '강의에 기반할 때 다음 중 성서에 등장한 물의 메타포와 가장 거리가 먼 것을 고르시오.'
    qa71 = "요단강"
    qa72 = "스틱스강"
    qa73 = "사막에서의 방황"
    qa74 = "홍해"
    qa75 = "모두 성서에서의 물의 메타포와 관련이 있다"
    q7 = SelectField(str(qq7.encode('utf-8')), choices = [('T', qa71), ('F2', qa72), ('F1', qa73), ('F3', qa74), ('F4', qa75), ('K', qa06) ], validators = [Required()])
    
    
    qq8 = '다음 []안의 글은 성경 구절의 일부를 수정한 것이다. 강의내용에 기반할 때 제시된 구절과 관련하여 가장 거리가 먼 추측을 한 사람을 고르시오. [또 하루는 하느님의 아들들이 와서 하나님 앞에 서고 사탄도 그들 가운데에 와서 하나님 앞에 서니 하나님께서 사탄에게 이르시되 네가 어디에서 왔느냐 사탄이 하나님께 대답하여 이르되 땅을 두루 돌아 여기저기 다녀왔나이다 (중략) 하나님께서 사탄에게 이르시되 네가 욥을 주의하여 보았느냐 (중략) 사탄이 이에 하나님 앞에서 물러가며 욥을 쳐서 그의 발바닥에서 정수리까지 종기가 나게 한지라]'
    qa81 = "A: 사탄은 신의 아들인가보네."
    qa82 = "B: 욥은 하나님의 사랑을 받지 않았을까?"
    qa83 = "C: 사탄은 하나님의 뜻에 따라서 욥을 시험했겠군."
    qa84 = "D: 욥은 아마 유혹에 빠지지 쉬운 나약한 인물이었을거야."
    qa85 = "E: 욥은 사탄의 예상과는 달리 하나님을 원망하지 않았을거야."
    q8 = SelectField(str(qq8.encode('utf-8')), choices = [('F1', qa81), ('F2', qa82), ('F3', qa83), ('T', qa84), ('F4', qa85), ('K', qa06) ], validators = [Required()])
    
    
    #답?
    qq9 = '다음은 예수가 세례를 받던 순간에 대한 묘사이다. 강의내용에 기반할 때 이와 관련해 잘못된 것을 고르시오.'
    qa91 = "A: 세례를 주는 사람이 예수를 치켜세웠다."
    qa92 = "B: 예수에게 세례를 주는 사람이 세례 요한이구나."
    qa93 = "C: 고통에 빠져있던 예수는 세례로 평안을 얻었다."
    qa94 = "D: 예수가 세례를 받을 때 비둘기 같은 성령이 모여들었다."
    qa95 = "E: 예수에게 세례를 준 사람은 예수보다 먼저 나타나 예수가 올 것을 예비한 존재이다."
    q9 = SelectField(str(qq9.encode('utf-8')), choices = [('F1', qa91), ('F2', qa92), ('F3', qa93), ('T', qa94), ('F4', qa95), ('K', qa06) ], validators = [Required()])
    
    

    #답?
    #단답형
    qq10 = '다음 []안의 글은 성서에 기록된 어떤 사건을 요약한 것이다. 이 글을 읽고 강의내용에 기반해 (a)와 (b)가 지칭하는 대상을 적으시오. [(a)가 광야로 가서 (b)에게 시험을 받았다. (b)는 (a)에게 \"네가 (c)의 아들이거든, 이 돌들에게 빵이 되라고 말해보아라."]'
    q10 = SelectField(str(qq10.encode('utf-8')), choices = [('F1', qa101), ('F2', qa102), ('F3', qa103), ('T', qa104), ('F4', qa105), ('K', qa06) ], validators = [Required()])
    
    
    #답
    qq11 = '다음은 성서의 일부이다. 강의 내용에 기반할 때 다음 구절이 의미하는 사건에 대한 설명과 거리가 먼 것을 고르시오.'
    qa111 = "A: 사탄은 신에게 반발하여 예수를 유혹하였으나 실패하였다."
    qa112 = "B: 예수가 이겨낸 첫번째 유혹은 물질 유혹이었다."
    qa113 = "C: "
    qa114 = "D: "
    qa115 = "E: "
    q11 = SelectField(str(qq11.encode('utf-8')), choices = [('F1', qa111), ('F2', qa112), ('F3', qa113), ('T', qa114), ('F4', qa115), ('K', qa06) ], validators = [Required()])
    
    

    
    
    