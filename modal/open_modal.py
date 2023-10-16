from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route('/')
def home():
    modal_urls = {
        'login_url': "{{ url_for('login') }}",
        'signup_url': "{{ url_for('signup') }}",
    }
    return render_template('base.html', modal_urls=modal_urls)


@app.route('/login')
def modal():
    return render_template('logged_in_modals.html')



if __name__ == '__main__':
    app.run(debug=True)