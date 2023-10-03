# routes related to authentication defined here
# blueprint of website (contains routes - URLs)
# render_template uses Jinja to finds template in 'templates' directory
# request allows access to request information
# flash allows a message to be flashed on the screen to the user via Jinja block - see login route below and block below nav on base.html
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User # imports User database
from werkzeug.security import generate_password_hash, check_password_hash # module to deal with hashing a password
from . import db # imports database (from __init__.py import db)
from flask_login import login_user, login_required, logout_user, current_user


# set up a blueprint for our application
auth = Blueprint('auth', __name__)


# login page
@auth.route('/login', methods=['GET', 'POST']) # argument here must match URL that is called (in this case from nav bar button href in base.html), unless prefixed when blueprint registered, methods defines what requests route can accept, default > 'GET' only
def login():

    # if request is a POST, get form information
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # queries database to check if we already have that user
        user = User.query.filter_by(email=email).first() # returns first (if any users found where email matches email provided in form)
        if user:
            if check_password_hash(user.password, password): # hashes provided password and checks against hashed password in database
                flash('Logged in successfully!', category='success')

                login_user(user, remember=True) # remembers user is logged in unless user clears browsing history or session or server restarts

                # redirects user to home page after logging in successfully
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user) 


# logout page
@auth.route('/logout')
@login_required # this makes sure route cannot be accessed unless user is logged in
def logout():
    logout_user() # logs out user using flask_login package
    return redirect(url_for('auth.login'))


# sign-up page
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':   # checks type of request method sent
        email = request.form.get('email')  # accesses request data that was sent as part of a form (specifically 'email' part) and assigns to 'email' var (which can be printed or used)
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # queries database to check if we already have that user
        user = User.query.filter_by(email=email).first() # returns first (if any users found where email matches email provided in form)

        # validation checks
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error') # flashes an error messsage to the user
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # creates new user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))

            # adds new user to database
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True) # remembers user is logged in unless user clears browsing history or session or server restarts

            flash('Account created!', category='success') # flashes success message to the user

            # finds url for home function and redirects user - could use '/' in url_for, but if ever change route, will stop working
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)