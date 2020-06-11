from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from project.config import Config


app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

# ENV = 'dev'
# if ENV == 'dev':
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/ming'
# else:
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nfzwobouvyyvbd:c8c02e3328191e1c081840212dbf10cb1a19bd9dc6b23736e813b59224f8fb31@ec2-52-70-15-120.compute-1.amazonaws.com:5432/dfv6v5e7ormli'


# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from project.users.routes import users
from project.posts.routes import posts
from project.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
