from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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

"""

below is the route import from blog the reason its below the 
code above is so that the app will aviod circular imports that
will through errors when trying to run the app.

"""

from blog import route