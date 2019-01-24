from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from blog import db, bcrypt
from blog.models import User, Post
from blog.users.forms import (RegistrationForm, LoginForm, UpdateProfileForm)
from blog.users.utils import save_picture

users = Blueprint('users', __name__)



"""

The route below is for the login page where users can use
there registration details from previous page to login to the 
user account.

The logic for the form is to check the email and password from the database
if the condition returns true then user will be login with alerted message,
if return false as the users email/password does not exist
then a flash message will be alerted.

"""

@users.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Login was successful. Happy posting', 'success')
            return redirect(url_for('users.account'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


"""

Below is the route for the user to logout and be redirected to
the login page.

I used bootstrap warining class for loging out.

"""

@users.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out successfuly', 'warning')
    return redirect(url_for('users.login'))


"""

The route below is for the user account details where user can
update there user info.
The form is so the user can update thier user profile info and image.
The image file url_for is being concatenated with the users updated
image.

The save_picture function is to save the image to the root path and 
I use secrets module to change the name of the image to numbers to avoid
image names clashing. Also the function resizes the image output for better performace
of the app.

You wont need to update email or username when updating the profile image.
You can also update username and email with out updating image.

"""

@users.route("/account", methods=['POST', 'GET'])
@login_required
def account():
    
    form= UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile has been upadate!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)
