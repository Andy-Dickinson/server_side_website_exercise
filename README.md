# server_side_website_exercise
Full examples of how to setup a server side website using flask and styling with bootstrap. Implements authentication, databases


main.py:
    run to start web-server / website


Directory 'website':
    stores all code for website - 

    __init__.py:
        makes 'website' directory a package so 'website' dir can be imported and files inside can run automatically

    views.py:
        store all views (URL endpoints) for front end aspect of website - routes

    auth.py:
        store all routes (URL endpoints) relating to authentication

        - sign_up.html:
            'Sign Up' form sends Post request

        - login.html:
            'Login' form sends POST request

    models.py:
        used to store database models

    * Directory 'static':
        stores static files (such as JS, CSS, img)
        
    * Directory 'templates':
        stores templates of pages 

        - base.html:
            defines theme to website (header/nav/footer) - this gets overridden by other html documents with more specific information

        - home.html, login.html, sign_up.html:
            extends base.html template

  