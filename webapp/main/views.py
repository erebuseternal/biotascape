from flask import render_template
from . import main

@main.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET'])
def login():
    site = "https://www.inaturalist.org"
    app_id = 'b52bd594b6f0a93cd2c45dc10f8bf165bb055d48dc64a2394c8b67f41dce1464'
    redirect_uri = 'https://localhost:5000/'
    url = f'{site}/oauth/authorize?client_id={app_id}&redirect_uri={redirect_uri}&response_type=code'
    return render_template('login.html', url=url)

@main.route('/naturalist_login', methods=['GET'])
def naturalist_login():
    return render_template('home.html')