"""
User Entity class representation

A User can use the system based in it's rol

"""


from utils.db import db
from models.user_rol import User_rol
from models.user_harvest import User_harvest
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model) :

    # User Attributes
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
    user_harvest_desc = db.Column(db.Integer, db.ForeignKey('user_harvest.description'))

    # User Class Constructor
    def __init__(self, name, last_name, username, email,\
         password, gender, date_of_birth, phone, address, user_rol_desc,user_harvest_descrip):
        self.name = name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.address = address
        self.user_rol_id = User_rol.getId(rol_description= user_rol_desc)
        self.user_harvest_desc = User_harvest.getId(description= user_harvest_descrip)
        self.set_password(password)

    # String representation or a User by its ID
    def __repr__(self):
        return '<Post %r >' % self.id

    # The password is encripted
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Indicates when a username is the database or not
    def is_user(username):
        return User.query.filter_by(username=username).first() != None

    # Given a password verify is correspond to the given user
    def verify_password( self, username, password ):
        if(self.is_user(username)):
            password_hashed = User.query.filter_by(username=username).first().password
            return check_password_hash(password_hashed, password)
        print("User not in Database")
        return False

    # Return the user rol given the username
    def get_user_rol_by_username( self, username ):
        user_rol_id = User.query.filter_by(username = username).first().user_rol_id
        user_rol = User_rol.query.get(user_rol_id).description
        return user_rol
