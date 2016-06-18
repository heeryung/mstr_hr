#Blueprint routes and views functions

from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
from flask.ext.login import login_user, logout_user, login_required, \
    current_user
from . import lecture
# from . import auth
from .. import db
from ..models import User
# from .forms import LoginForm, RegistrationForm, ChangePasswordForm,\
#     PasswordResetRequestForm, PasswordResetForm, ChangeEmailForm
from sqlalchemy.orm import load_only
from flask import g
from werkzeug import secure_filename


@lecture.route('/social')
def socialClue():
    return render_template('lecture/social.html')
    
def redirectSocial():
    return redirect(url_for('lecture.social'))    




