#Blueprint routes and views functions

from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
from flask.ext.login import login_user, logout_user, login_required, \
    current_user
# from . import lecture
from .. import db
from ..models import User, Permission, Role, Summary, PostSurvey_A, PostSurvey_B, PreSurvey, BrainSurvey, ReligionSurvey
from sqlalchemy.orm import load_only
from flask import g
# from .forms import PreSurveyForm, BrainForm, ReligionForm, PostSurvey_AForm, PostSurvey_BForm
from werkzeug import secure_filename
from flask.ext import admin, login
from flask.ext.admin import Admin
from flask.ext.admin.contrib import sqla
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash






