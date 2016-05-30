from flask import Blueprint

lecture = Blueprint('lecture', __name__)

from . import views

