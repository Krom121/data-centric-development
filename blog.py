from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

"""

The secret key was created using the python terminal.
by use the built in module sercrets and calling 
secrets.token_hex(16) don't forget the number

"""
app.config['SECRET_KEY'] = 'ceacbd61a815126f364fba1bc5ea2356'


"""

The route below is for the registration page where users first create 
there account.

"""

@app.route("/", methods=['POST', 'GET'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login')) 
    return render_template('index.html', title='Register', form=form)

"""

The route below is for the login page where users can use
there registration details from previous page to login to the 
user account.

"""

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()

    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)