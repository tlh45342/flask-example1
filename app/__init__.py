from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

#create app
app = Flask(__name__)
app.debug=True
login_manager = LoginManager(app)
login_manager.login_view = "login"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

from app import routes

#init packages
#login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

#import Blueprint
#from app.blueprints.user.routes import user

#from app import user
#from app import auth

class User(UserMixin):
    def __init__(self, id, email, password):
         print(id)
         self.id = id
         self.email = email
         self.password = password
         self.authenticated = False
    def is_active(self):
         return self.is_active()
    def is_anonymous(self):
         return False
    def is_authenticated(self):
         return self.authenticated
    def is_active(self):
         return True
    def get_id(self):
         return self.id
 