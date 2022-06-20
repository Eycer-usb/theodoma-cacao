from flask import Flask
from routes.auth import auth
from routes.admin import admin
from routes.user import user
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
db = "db.db"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)


app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(user)
app.secret_key = "#a@sKUGHkl[;][/=6095sKHGK-~gh`d=+p?*\ ~`z'.a&689Uh8bHahjashdbjHJKgsdsjaJKKJ"
