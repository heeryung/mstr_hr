#!/usr/bin/env python
# used to start the application
# the script begins by creating an application...
import os
from app import create_app, db
from app.models import User, Role, Permission, Summary, PostSurvey_A, PostSurvey_B, BrainSurvey, ReligionSurvey, PreSurvey
from flask import Flask
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext import admin, login
from flask.ext.admin import Admin
from flask.ext.admin.contrib import sqla
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash



app = create_app(os.getenv('MSTR_HR_CONFIG') or 'default')
manager = Manager(app)
manager.add_option('-c', '--config', dest='config', required=False)
migrate = Migrate(app, db)
admin = Admin(app, name='mstr_hr', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Summary, db.session))
admin.add_view(ModelView(PreSurvey, db.session))
admin.add_view(ModelView(ReligionSurvey, db.session))
admin.add_view(ModelView(BrainSurvey, db.session))
admin.add_view(ModelView(PostSurvey_A, db.session))
admin.add_view(ModelView(PostSurvey_B, db.session))


    
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

#unit test launcher command decorator makes it simple to implement custom commands.      
@manager.command


def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
if __name__ == '__main__':
    manager.run()
