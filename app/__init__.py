from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
#different level of security (strong = keep track of IP, browser agent, and log the user out if it detects a change)
login_manager.session_protection = 'strong'
# setting endpoint of login page (prefixed with the blueprint name)
login_manager.login_view = 'auth.login'



#the application factory, which takes as an argument the name of a configuration to use for the application
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)    

    
    #attach routes and custom error pages here
    #Blueprint registration
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    from .lecture import lecture as lecture_blueprint
    app.register_blueprint(lecture_blueprint, url_prefix='/lecture')
    
    return app
