from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask.ext


# permission constant
class Permission:
    GROUP_S = 0x01
    PLAY = 0x02
    QUIZ = 0X04
    ADMINISTRATOR = 0x80
    

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    #default should be True for only one rols and False for all the others
    default = db.Column(db.Boolean, default = False, index = True)
    #allowed -> 1 (administartion access )
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name
        
    @staticmethod
    def insert_roles():
        roles = {
            'Group_S' : (Permission.GROUP_S | 
                         Permission.PLAY |
                         Permission.QUIZ, True),
            'Group_N' : (Permission.PLAY |
                         Permission.QUIZ, True),
            'Administrator' : (0xff, False)
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
        return '<User %r>' % self.username
    
    


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    #login with their email
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#password    
    password_hash = db.Column(db.String(128))
#additional information
    code = db.Column(db.String(64), unique=True, index=True)
    age = db.Column(db.Integer, unique=True, index=True)
    sex = db.Column(db.String(40), index=True)

    confirmed = db.Column(db.Boolean, default=False)


    def __init__(self, **kwargs):
        #Group_S constructor: invoking the constructors of the base classes, and if after that the object does not have a role defined, it sets the administrator or default roles depending on the email address
        super(Group_S, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()
                
    
#generate a token with a default validity time of one hour
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({ 'confirm': self.id })
            
    
#verifies token and, if valid, sets the new confirmed attribute to True
    def confirm(self, token) :
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except :
            return False
        if data.get('confirm') !=self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
        
# after every new account is added, a new database migration needs to be generated and applied.
        
    
    #define a default role for users
   
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
        return self.role is not None and \ (self.role.permissions % permisssions) == permissions
        
    def is_administrator(self):
        return self.can(Permission.ADMINISTER)
        
    def __repr__ (self):
        return '<Group_S %r'> % self.usernmae
            

        
class  AnonumousUser(AnonumousUserMixin):
    def can(self, permissions):
        return False
    
    def is_administrator(self):
        return False
        
login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
