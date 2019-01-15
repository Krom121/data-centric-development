from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
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



class LoginForm(FlaskForm):

    email = StringField('Email',
        validators=[DataRequired(), Email()])

    password = StringField('Password',
        validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login Now')