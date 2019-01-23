from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User


"""

Registration from below to let users register before loging in
The function below the class is to validate the field
in light of users creating the same username and email.

by querying the database for username/email that it's not the same as
another.Dose not exist or existing.

"""

class RegistrationForm(FlaskForm):
    username = StringField('Username',
        validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
        validators=[DataRequired(), Email()])

    password = StringField('Password',
        validators=[DataRequired()])

    confirm_password = StringField('confirm_Password',
        validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Join Today')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username has been taken. Please choose another')
    
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email has been taken. Please choose another')


"""

below is the form class for the login form
It's very common for users to be asked for their email as the 
user is more likely to remember their email address other than 
a username

"""
class LoginForm(FlaskForm):

    email = StringField('Email',
        validators=[DataRequired(), Email()])

    password = StringField('Password',
        validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login Now')

"""

below is the form for updating the user profile

"""

class UpdateProfileForm(FlaskForm):
    username = StringField('Username',
        validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
        validators=[DataRequired(), Email()])

    picture = FileField('Update profile image',
        validators=[FileAllowed(['png', 'jpg'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username has been taken. Please choose another')
    
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email has been taken. Please choose another')


"""
below is the postform for users to create a post 

"""
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    content = TextAreaField('Blog Content', validators=[DataRequired()])

    submit = SubmitField('Post')