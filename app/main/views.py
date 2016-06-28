#the routes of the application updated to be in the blueprint
#imports blueprint and defines the routes associated with authentication using its route decorator
from datetime import datetime
from flask import render_template, session, redirect, url_for, request, current_app, abort, flash, g
from flask.ext.login import login_user, logout_user, login_required, \
    current_user, abort
from . import main
from .forms import SummaryForm, NameForm, PreSurveyForm, ReligionForm, PostSurvey_AForm, PostSurvey_BForm
from .. import db
from ..models import User, Permission, Role, Summary, PreSurvey, PostSurvey_A, PostSurvey_B, ReligionSurvey
from ..decorators import admin_required
from flask.ext import admin, login
from flask.ext.admin.contrib import sqla
from flask.ext.admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash







# view function passes the form and the complete list of blog posts to the template.
@main.route('/', methods=['GET', 'POST'])
def index():
    form = SummaryForm()
    if current_user.can(Permission.WRITE_ARTICLES) and \
            form.validate_on_submit():
        summary = Summary(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(summary)
        return redirect(url_for('.index'))
    
    # Paginate the blog post list
    page = request.args.get('page', 1, type=int)
    pagination = Summary.query.order_by(Summary.timestamp.desc()).paginate(page, per_page=current_app.config['MSTR_HR_SUMMARIES_PER_PAGE'], error_out=False)
    summaries = pagination.items
    return render_template('index.html', form=form, summaries=summaries,
                           pagination=pagination)    
        

@main.route('/<username>/')
@login_required
def user(username):
    user = User.query.filter_by(username = username).first()
    # if user or code is None:
    if user is None :
        abort(404)
        
    summaries = user.summaries.order_by(Summary.timestamp.desc()).all()
    return render_template('lecture/class_home.html', user=user, summaries=summaries)
       #the list of posts for a user : obtained from the User.posts.relationship, which is a query object, so filters such as order_by() can be used in it as well

 

        
            

@main.route('/<username>/lecture/<filename>', methods = ['GET', 'POST'])    
@login_required
def userFile(username, filename) :
    form = SummaryForm()
    if request.method == 'POST' and form.validate_on_submit():
        # summary = Summary(body=form.body.data, author=current_user._get_current_object())
        summary = Summary(body=form.body.data)
        db.session.add(summary)
        # return redirect(url_for('.index'))
                
    page = request.args.get('page', 1, type=int)
    pagination = Summary.query.order_by(Summary.timestamp.desc()).paginate(
        page, per_page=current_app.config['MSTR_HR_SUMMARIES_PER_PAGE'], error_out=False)
    summaries = pagination.items
   
    return render_template('lecture/' + filename, user = user, form=form, summaries=summaries, pagination=pagination)




@main.route('/survey/pre_survey.html', methods = ['GET', 'POST']) 
@login_required
def preSurvey():
    form = PreSurveyForm(request.form)
    
    if request.method == 'POST' and form.validate_on_submit():
        preSurvey = PreSurvey()
        form.populate_obj(preSurvey)
        db.session.add(preSurvey)
        db.session.commit()
    
    return render_template('survey/preSurvey.html', title='Pre_Survey', form=form)



    

@main.route('/survey/post_survey_a', methods = ['GET', 'POST'])
@login_required
def postSurvey_A():
    form = PostSurvey_AForm(request.form)
    
    if request.method == 'POST' and form.validate_on_submit():
        postSurvey_a = PostSurvey_A()
        form.populate_obj(postSurvey_a)
        db.session.add(postSurvey_a)
        db.session.commit()

    return render_template('survey/postSurvey_a.html', title='Survey A', form=form)
# else:
#     return redirect(url_for('/post_survey', user = user, form = form))

@main.route('/survey/post_survey_b', methods = ['GET', 'POST'])
@login_required
def postSurvey_B():
    form = PostSurvey_BForm(request.form)
    
    if request.method == 'POST' and form.validate_on_submit():
        postSurvey_b = PostSurvey_B()
        form.populate_obj(postSurvey_b)
        db.session.add(postSurvey_b)
        db.session.commit()

    return render_template('survey/postSurvey_b.html', title='Survey B', form=form)
    

@main.route('/survey/religion_survey', methods = ['GET', 'POST'])
@login_required
def religionSurvey():
    form = ReligionForm(request.form)
    
    if request.method == 'POST' and form.validate_on_submit():
        religionSurvey = ReligionSurvey()
        form.populate_obj(religionSurvey)
        db.session.add(religionSurvey)
        db.session.commit()

    return render_template('survey/religionSurvey.html', title='ReligionSurvey', form=form)


@main.route('/survey/survey_final.html')
@login_required
def finalSurvey():
    return render_template('survey/survey_final.html', title='Survey fin')
    


# the route and view function that support permanent links are shown
@main.route('/summary/<int:id>')
def summary(id):
    summary = Summary.query.get_or_404(id)
    return render_template('lecture/summary.html', summary=[summary])



