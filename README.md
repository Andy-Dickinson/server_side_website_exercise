# server_side_website_exercise
Full examples of how to setup a server side website using flask and styling with bootstrap. Implements authentication, databases


main.py:
    run to start web-server / website, calls create_app() in __init__.py


Directory 'website':
    stores all code for website - 

    __init__.py:
        makes 'website' directory a package so 'website' dir can be imported and files inside can run automatically.
        create_app():
            creates a Flask app, iniitialises secret key, registers blueprints, adds prefixes, imports db models, creates db, initialises login manager, redirects user to login page when not logged in ('/' route otherwise), defines load_user callback function and returns app
        create_database(app):
            called from within create_app(), creates app if does not exist

    auth.py:
        store all routes (URL endpoints) relating to authentication

        - route('/login'):
            gets form data if 'POST', queries db, hashes and checks password, remembers user, redirects to 'views.home'. 
            renders 'login.html'

        - route('/logout'):
            logs out user, redirects to 'auth.login'

        - route('/sign-up'):
            gets form data if 'POST', queries db, validation checks, creates new_user generating password hash, adds user to db, logs in user, redirects to 'views.home'. 
            renders 'sign_up.html'

    views.py:
        store all views (URL endpoints) for front end aspect of website - routes

        - route('/'):
            if 'POST', adds new note to db.
            renders 'home.html'

        - rounte('/delete-note'):
            accepts 'POST' requests only, used to delete note from db, called from deleteNote() in index.js

    models.py:
        used to store database models

        - Note(db.Model):
            used to store notes

        - User(db.Model, UserMixin):
            used to store user details and defines user relationship to Note

    * Directory 'static':
        stores static files (such as JS, CSS, img)

        - index.js:
            function deleteNote(noteId) sends 'POST' request to endpoint '/delete-note' followed by reloading window to home page ('/')
        
    * Directory 'templates':
        stores templates of pages 

        - base.html:
            defines theme to website (header/nav/footer) - this gets overridden by other html documents with more specific information
            has collapsable navbar, if statements to show 'Home'/'Logout' if logged in, 'Login'/'Sign Up' otherwise
            defines templates for title, flash messages, and content

        - home.html, login.html, sign_up.html:
            extends base.html template
            login.html/sign_up.html defines relevant forms
            home.html loops and displays notes, button to delete notes(calls deleteNote() function in index.js), form method to 'POST' new notes

  