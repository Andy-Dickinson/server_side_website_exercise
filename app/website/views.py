# blueprint of website (contains routes - URLs)
from flask import Blueprint, render_template
from flask_login import login_required, current_user

# set up a blueprint for our application
views = Blueprint('views', __name__)


# defines routes for views

# home page route (using blueprint 'views')
@views.route('/') # argument here must match URL that is called (unless prefixed when blueprint registered), argument 'methods=[]' defines what type of requests that route can accept - default > can only accept 'GET' requests
@login_required # this means home page cannot be accessed unless logged in
def home():
    return render_template("home.html") # 1st argument here must match filename of html file in 'templates' directory, sub-directories should be prepended either here or when blueprint registered
    # following arguments are variables which can be accessed from within the templates using Jinja {{ var ... restricted Python code }}