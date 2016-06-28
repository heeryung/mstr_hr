from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
from flask import current_app, request
from flask.ext.login import UserMixin, AnonymousUserMixin
from . import db, login_manager
from flask.ext import admin, login
from flask.ext.admin.contrib import sqla
from flask.ext.admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash


    



class Permission:
    # GROUP_S = 0x01
    # PLAY = 0x02
    # QUIZ = 0X04
    WRITE_ARTICLES = 0x08
    ADMINISTER = 0x80



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.WRITE_ARTICLES, True),
            'Administrator': (0xff, False)
        }
        
        for r in roles :
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()
        
    def __repr__(self):
        return '<Role %r>' % self.name
    
    

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
#additional information     
    code = db.Column(db.String(64), unique=True, index=True)
    age = db.Column(db.Integer,  index=True)
    sex = db.Column(db.String(40), index=True)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
#Survey (...?)
    # s_pre = db.Column(db.Boolean)
    # s_post = db.Column(db.Boolean)
    # s_brain = db.Column(db.Boolean)
    # s_religion = db.Column(db.Boolean)
#relationship
    summaries = db.relationship('Summary', backref = 'author', lazy = 'dynamic')
    # religionSurveys = db.relationship('ReligionSurvey', backref = 'author', lazy = 'dynamic')
    # brainSurveys = db.relationship('BrainSurvey', backref = 'author', lazy = 'dynamic')
    # preSurveys = db.relationship('PreSurvey', backref = 'author', lazy = 'dynamic')
    # postSurveys_a = db.relationship('PostSurvey_A', backref = 'author', lazy = 'dynamic')
    # postSurveys_b = db.relationship('PostSurvey_B', backref = 'author', lazy = 'dynamic')
    #
        #Group_S constructor: invoking the constructors of the base classes, and if after that the object does not have a role defined, it sets the ADMINISTER or default roles depending on the email address
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['MSTR_HR_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()
                
                
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username
        

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def __repr__(self):
        return '<User %r>' % self.username



            
            

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()


# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))




class PreSurvey(db.Model):
    __tablename__ = 'preSurveys'
    id = db.Column(db.Integer, primary_key=True)
    rq_int = db.Column(db.String(20))
    rq_know = db.Column(db.String(20)) 
    timestamp = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', uselist=False, backref='PreSurvey')
        
        
    # def __init__(self, rq_int=None, rq_know=None):
    #     self.rq_int = rq_int
    #     self.rq_know = rq_know




class PostSurvey_A(db.Model):
    __tablename__ = 'postSurveys_a'
    id = db.Column(db.Integer, primary_key=True)
    helpful_a = db.Column(db.String(20))
    useful_a = db.Column(db.String(20))
    curious_a = db.Column(db.String(20))    
    satisfy_a = db.Column(db.String(20))    
    annoy_a = db.Column(db.String(20))    
    frustrated_a = db.Column(db.String(20))    
    timestamp = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', uselist=False, backref='PostSurvey_A')


    def __init__(self, helpful_a=None, useful_a=None, curious_a=None, satisfy_a=None, annoy_a=None, frustrated_a=None):
        self.helpful_a = helpful_a
        self.useful_a = useful_a
        self.curious_a = curious_a
        self.satisfy_a = satisfy_a
        self.annoy_a = annoy_a
        self.frustrated_a = frustrated_a





class PostSurvey_B(db.Model):
    __tablename__ = 'postSurveys_b'
    id = db.Column(db.Integer, primary_key=True)
    helpful_b = db.Column(db.String(20))
    useful_b = db.Column(db.String(20))
    curious_b = db.Column(db.String(20))    
    satisfy_b = db.Column(db.String(20))    
    annoy_b = db.Column(db.String(20))    
    frustrated_b = db.Column(db.String(20))    
    gender = db.Column(db.String(20))    
    age = db.Column(db.String(20))    
        
    timestamp = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', uselist=False, backref='PostSurvey_B')


    def __init__(self, helpful_b=None, useful_b=None, curious_b=None, satisfy_b=None, annoy_b=None, frustrated_b=None, gender=None, age=None):
        self.helpful_b = helpful_b
        self.useful_b = useful_b
        self.curious_b = curious_b
        self.satisfy_b = satisfy_b
        self.annoy_b = annoy_b
        self.frustrated_b = frustrated_b
        self.gender = gender 
        self.age = age
    


    
#
# class BrainSurvey(db.Model):
#     __tablename__ = 'brainSurveys'
#     id = db.Column(db.Integer, primary_key=True)
#     answer = db.Column(db.String(100))
#     timestamp = db.Column(db.DateTime, index=True, default = datetime.utcnow)
#     author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship('User', uselist=False, backref='BrainSurvey')



class ReligionSurvey(db.Model):
    __tablename__ = 'religionSurveys'
    id = db.Column(db.Integer, primary_key=True)
    rq1 = db.Column(db.String(20))
    rq2 = db.Column(db.String(20))
    rq3 = db.Column(db.String(20))
    rq4 = db.Column(db.String(20))
    rq5 = db.Column(db.String(20))
    rq6 = db.Column(db.String(20))
    rq7 = db.Column(db.String(20))
    rq8 = db.Column(db.String(20))
    rq9 = db.Column(db.String(20))
    rq10 = db.Column(db.String(20))
    rq11 = db.Column(db.String(20))
    rq12 = db.Column(db.String(20))
    rq13 = db.Column(db.String(20))
    rq14 = db.Column(db.String(20))
    rq15 = db.Column(db.String(20))
            
    timestamp = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', uselist=False, backref='ReligionSurvey')

    def __init__(self, rq1=None, rq2=None, rq3=None, rq4=None, rq5=None, rq6=None, rq7=None, rq8=None, rq9=None, rq10=None, rq11=None, rq12=None, rq13=None, rq14=None, rq15=None):
        self.rq1 = rq1
        self.rq2 = rq2
        self.rq3 = rq3
        self.rq4 = rq4
        self.rq5 = rq5
        self.rq6 = rq6
        self.rq7 = rq7
        self.rq8 = rq8
        self.rq9 = rq9
        self.rq10 = rq10
        self.rq11 = rq11
        self.rq12 = rq12
        self.rq13 = rq13
        self.rq14 = rq14
        self.rq15 = rq15


    
    

class Summary(db.Model):
    __tablename__ = 'summaries'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    


