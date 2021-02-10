import os
from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth

bootstrap = Bootstrap()
db = SQLAlchemy()
oauth = OAuth()
oauth.register('inaturalist', {...})

def create_app():
    app = Flask(__name__)
    
    # used by flask-login
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    app.config['INATURALIST_CLIENT_ID'] = os.environ['APPLICATION_ID']
    app.config['INATURALIST_CLIENT_SECRET'] = os.environ['APPLICATION_SECRET']
    app.config['INATURALIST_ACCESS_TOKEN_URL'] = 'https://www.inaturalist.org/oauth/token'
    app.config['INATURALIST_AUTHORIZE_URL'] = 'https://www.inaturalist.org/oauth/authorize'
    
    db.init_app(app)
    bootstrap.init_app(app)
    oauth.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .models import User   
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app

app = create_app()