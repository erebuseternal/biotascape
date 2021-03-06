from flask import render_template
from flask_login import login_required, current_user
from . import main

@main.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name,
                           access_token=current_user.access_token)