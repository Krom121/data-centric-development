from flask import render_template, request, Blueprint
from blog.models import Post
from flask_login import current_user
from blog.users.forms import RegistrationForm

main = Blueprint('main', __name__)

"""

The route below is for the registration page where users first create 
there account.The logic will generate a password as a string-(decode)
and commit the username and email to the database.
current_user is to authenticate current user so when login
the user will only see the account details page logout and
new and old post plus the user will be able to create own posts.

For testing purposes i redirect the user back from the login form to the
registration form this is just for manual testing to ensure all the code works as
expected and validation messages are working.

"""

@main.route("/", methods=['POST', 'GET'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now login', 'success')
        return redirect(url_for('users.login')) 
    return render_template('index.html', title='Register', form=form)