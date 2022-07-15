"""
Set up the flask app configuration
here is the database connection setting
and where the routes are registered

"""


from flask import Flask
from routes.auth import auth
from routes.user_rol import user_rol
from routes.user import user
from routes.productor import productor_route
from routes.productor_type import productor_type_route
from routes.harvest import harvest_route
from routes.purchase import purchase
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
    app.register_blueprint(user_rol)
    app.register_blueprint(productor_route)
    app.register_blueprint(productor_type_route)
    app.register_blueprint(user)
    app.register_blueprint(harvest_route)
    app.register_blueprint(purchase)
    app.secret_key = "#a@sKUGHkl[;][/=6095sKHGK-~gh`d=+p?*\ ~`z'.a&689Uh8bHahjashdbjHJKgsdsjaJKKJ"

    return app
