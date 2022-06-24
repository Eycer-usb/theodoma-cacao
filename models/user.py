"""
User Entity class representation

The user rols is a abstraction to diferent
users permissions. The admin is the hightest
rol in the jerarquic structure
"""


from utils.db import db
from models.user_rol import User_rol
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model) :
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    username = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(100), nullable = True)
    password = db.Column(db.String(100), nullable = False)
    gender = db.Column(db.String(10), nullable = False)
    date_of_birth = db.Column(db.String(10), nullable = False)
    phone = db.Column(db.String(20), nullable = True)
    address = db.Column(db.String(150), nullable = True)
    user_rol_id = db.Column(db.Integer, db.ForeignKey('user_rol.id'))


    def __init__(self, name, last_name, username, email,\
         password, gender, date_of_birth, phone, address, user_rol_desc):
        self.name = name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.address = address
        self.user_rol_id = User_rol.getId(rol_description= user_rol_desc)
        self.set_password(password)

    def __repr__(self):
        return '<Post %r >' % self.id

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def is_user(username):
        return User.query.filter_by(username=username).first() != None

    def verify_password( self, username, password ):
        if(self.is_user(username)):
            password_hashed = User.query.filter_by(username=username).first().password
            return check_password_hash(password_hashed, password)
        print("User not in Database")
        return False
    def get_user_rol_by_username( self, username ):
        user_rol_id = User.query.filter_by(username = username).first().user_rol_id
        user_rol = User_rol.query.get(user_rol_id).description
        return user_rol
