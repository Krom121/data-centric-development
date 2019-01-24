import os

class Config:

    """
    The secret key was created using the python terminal.
    by use the built in module sercrets and calling 
    secrets.token_hex(16) don't forget the number

    """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    

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

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')