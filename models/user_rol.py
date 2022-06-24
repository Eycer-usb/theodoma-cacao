"""
User Rol Entity class representation

The user rols is a abstraction to diferent
users permissions. The admin is the hightest
rol in the jerarquic structure
"""

from utils.db import db

class User_rol(db.Model):

    # User Rol Attributes
    __tablename__ = 'user_rol'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), nullable = False)
    str_description = db.Column(db.String(50), nullable = False)

    # User Rol Class Constructor
    def __init__(self, description, str_description = description):
       self.description = description
       self.str_description = str_description

    # Given a rol description, is query the database and 
    # then return the correct id
    def getId(rol_description):
        return User_rol.query.filter_by(description=rol_description).first().id