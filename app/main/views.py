#the routes of the application updated to be in the blueprint
#imports blueprint and defines the routes associated with authentication using its route decorator
from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required, \
    current_user
from . import main
from .forms import NameForm
from .. import db
from ..models import User




    

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())
    
    
    
    

@main.route('/user/<username>/')
@login_required
# def user(username, codename):
def user(username):
    user = User.query.filter_by(username = username).first()
    # if user or code is None:
    if user is None :
        abort(404)

    if username[0] == "S" :
        return render_template('lecture/class_s.html', user=user)
    else :
        return render_template('lecture/class_n.html', user=user)


    summaries = user.summaries.order_by(Summary.timestamp.des()).all()
    return render_template('summary.html', user=user, summaries=summaries)


# test page route with blog posts
@main.route('/user/<username>/summary')
@login_required
def summary(username) :
    user = User.query.filter_by(username = username).first()
    if user is None :
        abort(404)
        
    summaries = user.posts.order_by(Summary.timestamp.desc()).all()
    return render_template('summary.html', user=user, summaries=summaries)
    
    


