from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# initialises database
db = SQLAlchemy()
# creates database object
DB_NAME = "database.db"


# creates a Flask app, iniitialises secret key, registers blueprints, adds prefixes and returns app
def create_app():
    app = Flask(__name__) # initialises Flask
    app.config['SECRET_KEY'] = 'sdfsfs'  # secret key for app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # tells flask where database is located

    db.init_app(app) # tells alchemy this is the app we will use with this database

    # register routes/views blueprints
    from .views import views
    from .auth import auth

    # optional url_prefix (adds prefix to url between host and route path) 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    # imports database models - imports required in this file so models.py file is loaded before we try to create any databases
    from .models import User, Note
    
    create_database(app)

    # initialises login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # where flask should redirect if not logged in
    login_manager.init_app(app) # tells login manager which app we are using

    # load users
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # gets primary key and checks is equal to int version of id passed as argument

    return app


# creates database which will be stored in 'instance' directory
def create_database(app):

    # passes app configurations and checks if the app is availiable
    with app.app_context():

        # checks if database exists
        if not path.exists('website/' + DB_NAME):
            db.create_all() # creates database if doesn't exist
            print('Createed Database!')