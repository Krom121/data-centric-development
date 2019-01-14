from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post


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
