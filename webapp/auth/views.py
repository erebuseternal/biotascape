from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from ..models import User
from .. import db
from .. import oauth

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    
    new_user = User(email=email, name=name, 
                    password=generate_password_hash(password, method='sha256'))
    
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Please try again.')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=True)
    return redirect(url_for('main.profile'))

@auth.route('/authenticate')
@login_required
def authenticate():
    redirect_uri = url_for('auth.callback', _external=True)
    return oauth.inaturalist.authorize_redirect(redirect_uri)

@auth.route('/authenticate/callback')
@login_required
def callback():
    token = oauth.inaturalist.authorize_access_token()
    access_token = token['access_token']
    current_user.access_token = access_token
    db.session.commit()
    return redirect(url_for('main.profile'))

