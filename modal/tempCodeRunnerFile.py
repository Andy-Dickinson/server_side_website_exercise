from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('base.html')


@app.route('/login')
def modal():
    return render_template('logged_in_modals.html')



if __name__ == '__main__':
    app.run(debug=True)