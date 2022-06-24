"""
Set up the flask app configuration
here is the database connection setting
and where the routes are registered

"""


from flask import Flask
from routes.auth import auth
from routes.admin import admin
from routes.user import user
from routes.shopping_analyst import shp_analyst
from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)
    db = "database.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    SQLAlchemy(app)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(shp_analyst)
    app.register_blueprint(user)
    app.secret_key = "#a@sKUGHkl[;][/=6095sKHGK-~gh`d=+p?*\ ~`z'.a&689Uh8bHahjashdbjHJKgsdsjaJKKJ"

    return app
