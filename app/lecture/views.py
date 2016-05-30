#Blueprint routes and views functions

from flask import render_template, redirect, request, url_for, flash, jsonify
from flask.ext.login import login_user, logout_user, login_required, \
    current_user
from . import lecture
# from . import auth
from .. import db
from ..models import User
from .forms import LoginForm
from sqlalchemy.orm import load_only
from flask import g

@lecture.route('/index')
def switching():
    form = LoginForm()
    u_email = form.email.data
    session.query(db).options(load_only("code"))
    
    if User.query.filter_by(email=field.data).first(): 
        if code[:1] is 'n' :
            return render_template('lecture/class_n.html', form=form)
        elif code[:1] is 's' :
            return render_template('lecture/class_s.html', form=form)    
        
    else:
        raise ValidationError('Your email is not regiseterd.')

@login_required
def secret():
    return 'Please do login. Only authenticated users are allowed.'


    
