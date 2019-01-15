from datetime import datetime
from blog import db, login_manager
from flask_login import UserMixin

"""

setting up the login manager

"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""

below is the model class for the database to create the
user table and allow users to be commited to the database

"""
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

"""

below is the model class for the database to create the
post table and allow users to be commited post to the database

This is the first relationship between user and post.
One author many posts
"""

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"
