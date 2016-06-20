#the routes of the application updated to be in the blueprint
#imports blueprint and defines the routes associated with authentication using its route decorator
from datetime import datetime
from flask import render_template, session, redirect, url_for, request, current_app, abort, flash
from flask.ext.login import login_user, logout_user, login_required, \
    current_user, abort
from . import main
from .forms import SummaryForm, QuizForm, NameForm
from .. import db
from ..models import User, Permission, Role, Summary, Quiz
from ..decorators import admin_required




@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())
    
        

@main.route('/<username>/')
@login_required
def user(username):
    user = User.query.filter_by(username = username).first()
    # if user or code is None:
    if user is None :
        abort(404)

    #the list of posts for a user : obtained from the User.posts.relationship, which is a query object, so filters such as order_by() can be used in it as well

    return render_template('lecture/class_home.html', user=user)
    



@main.route('/<username>/<filename>', methods = ['GET', 'POST'])    
@login_required
def userFile(username, filename) :
    user = User.query.filter_by(username = username).first()
    # if user or code is None:
    if user is None :
        abort(404)

    # return render_template('lecture/summary.html', )
    
    form = SummaryForm()
    if current_user.can(Permission.WRITE_ARTICLES) and \
            form.validate_on_submit():
        summary = Summary(body=form.body.data, author=current_user._get_current_object())
        db.session.add(summary)
        return redirect(url_for('.summary'))
    page = request.args.get('page', 1, type=int)
    pagination = Summary.query.order_by(Summary.timestamp.desc()).paginate(
        page, per_page=current_app.config['MSTR_HR_SUMMARIES_PER_PAGE'],
        error_out=False)
    summaries = pagination.items

        
   
    return render_template('lecture/' + filename, user = user, form=form, summaries=summaries,
                           pagination=pagination)
       

def redirectHtml(username, filename):
        return redirect(url_for(withUsername))        



def summary(username, filename) :
    user = User.query.filter_by(username = username).first()
    if user is None :
        abort(404)
# summary page route with blog posts
    summaries = user.summaries.order_by(Summary.timestamp.desc()).all()
    return render_template('lecture/summary.html', user=user, summaries=summaries)




# summary
# @login_required
# def summaryIndex():
#     form = SummaryForm()
#     if current_user.can(Permission.WRITE_ARTICLES) and \
#             form.validate_on_submit():
#         summaries = Summary(body=form.body.data, author=current_user._get_current_object())
#         db.session.add(summary)
#         return redirect(url_for('.summary'))
#     page = request.args.get('page', 1, type=int)
#     pagination = Summary.query.order_by(Summary.timestamp.desc()).paginate(
#         page, per_page=current_app.config['MSTR_HR_SUMMARIES_PER_PAGE'],
#         error_out=False)
#     summariess = pagination.items
#     return render_template('summary.html', form=form, summaries=summaries,
#                            pagination=pagination)
#
#
#
# def summary(username) :
#     user = User.query.filter_by(username = username).first()
#     if user is None :
#         abort(404)
#
#     summaries = user.summariess.order_by(Summary.timestamp.desc()).all()
#     return render_template('summary.html', user=user, summaries=summaries)#
#
# # test page route with blog posts
#
# @main.route('/<username>/summary', methods=['GET', 'POST'])
# pass the form and the complete list of blog posts to the template
# def userSummary(username):
#     user = User.query.filter_by(username = username).first()
#     # if user or code is None:
#     if user is None :
#         abort(404)
#
#     form = SummaryForm()
#     if current_user.can(Permission.WRITE_ARTICLES) and \
#             form.validate_on_submit():
#         summary = Summary(body=form.body.data, author=current_user._get_current_object())
#         db.session.add(summary)
#         return redirect(url_for('.summary'))
#     page = request.args.get('page', 1, type=int)
#     pagination = Summary.query.order_by(Summary.timestamp.desc()).paginate(
#         page, per_page=current_app.config['MSTR_HR_SUMMARIES_PER_PAGE'],
#         error_out=False)
#     summaries = pagination.items
#     return render_template('lecture/summary.html', form=form, summaries=summaries,
#                            pagination=pagination)
#
#
#
# def summary(username) :
#     user = User.query.filter_by(username = username).first()
#     if user is None :
#         abort(404)
# # summary page route with blog posts
#     summaries = user.summaries.order_by(Summary.timestamp.desc()).all()
#     return render_template('lecture/summary.html', user=user, summaries=summaries)
#


# @main.route('/<username>/quiz', methods=['GET', 'POST'])
# @login_required

