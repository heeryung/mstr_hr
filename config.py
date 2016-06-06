import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MSTR_HR_ADMIN = os.environ.get('MSTR_HR_ADMIN')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'heeryung.c@gmail.com'
    MAIL_PASSWORD = 'saucjeipaujfvdck'
    MSTR_HR_MAIL_SUBJECT_PREFIX = '[EXPRMNT]'
    MSTR_HR_MAIL_SENDER = 'MSTR_HR Admin <heeryung.c@gmail.com>'

    #administrator list
    ADMINS = ['heeryung.c@gmail.com']

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
        
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        
config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig, 
    'production' : ProductionConfig,
    
    'default' : DevelopmentConfig
}
    