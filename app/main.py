# imports website package and runs content of __init__ file (initialises Flask app)
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # only if we run this file (ie not if we import this file) will this be executed
    # debut should be set to false when running in production - when true, resets server every time a change is made and saved