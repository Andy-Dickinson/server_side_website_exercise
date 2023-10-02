# routes related to authentication defined here
# blueprint of website (contains routes - URLs)
# render_template uses Jinja to finds template in 'templates' directory
from flask import Blueprint, render_template

# set up a blueprint for our application
auth = Blueprint('auth', __name__)


# login page
@auth.route('/login') # argument here must match URL that is called (in this case from nav bar button href in base.html)
def login():
    return render_template("login.html", boolean=True) 


# logout page
@auth.route('/logout')
def logout():
    return "<p>logout</p>"


# sign-up page
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")