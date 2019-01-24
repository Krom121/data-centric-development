from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

"""
below is the postform for users to create a post 

"""
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    content = TextAreaField('Blog Content', validators=[DataRequired()])

    submit = SubmitField('Post')