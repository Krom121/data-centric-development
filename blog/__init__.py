from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

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

Bcrypt is being used to generate user passwords and encrypt
them in the database for sercurity.

"""

bcrypt = Bcrypt(app)

"""

below is the instance for the login manager and
login required

"""

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

"""

below is the route import from blog the reason its below the 
code above is so that the app will aviod circular imports that
will through errors when trying to run the app.

Now the app has been made into blueprints the routes have changed
below

"""

from blog.users.routes import users
from blog.posts.routes import posts
from blog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)