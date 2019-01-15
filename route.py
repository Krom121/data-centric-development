import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm, UpdateProfileForm
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
    flash('You have been logged out successfuly', 'warning')
    return redirect(url_for('login'))

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

"""

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', picture_fn)
    
    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn

@app.route("/account", methods=['POST', 'GET'])
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
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)