from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

"""

The secret key was created using the python terminal.
by use the built in module sercrets and calling 
secrets.token_hex(16) don't forget the number

"""

app.config['SECRET_KEY'] = 'ceacbd61a815126f364fba1bc5ea2356'

"""

below is the creation of the database for development purposes it
will SQLite. To create an instance of SQLite open python terminal 
and import the db from the main app 

>>>from blog import db
>>>db.create_all() This will create the instance

                OR

>>>from blog.models import db If there is a models.py file
>>>db.create_all() This will create the instance


"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    email = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"


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