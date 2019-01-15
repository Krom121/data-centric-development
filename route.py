from flask import render_template, url_for, flash, redirect, request
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


"""

The route below is for the registration page where users first create 
there account.The logic will generate a password as a string-(decode)
and commit the username and email to the database.
current_user is to authenticate current user so when login
the user will only see the account details page logout and
new and old post plus the user will be able to create own posts.

For testing purposes i redirect the user back from the login form to the
registration form tis is just for manual testing to ensure all the code works as
expected and validation messages are working.

"""

@app.route("/", methods=['POST', 'GET'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now login', 'success')
        return redirect(url_for('login')) 
    return render_template('index.html', title='Register', form=form)

"""

The route below is for the login page where users can use
there registration details from previous page to login to the 
user account.

The logic for the form is to check the email and password from the database
if the condition returns true then user will be login with alerted message,
if return false as the users email/password does not exist
then a flash message will be alerted.

"""

@app.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Login was successful. Happy posting', 'success')
            return redirect(url_for('account'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

"""

The route below is for the user account details where user can
update there user info

"""

@app.route("/account", methods=['POST', 'GET'])
@login_required
def account():

    return render_template('account.html', title='Account')