from flask import Flask


# creates a Flask app, iniitialises secret key and returns app
def create_app():
    app = Flask(__name__) # initialises Flask
    app.config['SECRET_KEY'] = 'sdfsfs'  # secret key for app


    # register routes/views blueprints
    from .views import views
    from .auth import auth

    # optional url_prefix (adds prefix to url between host and route path) 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app