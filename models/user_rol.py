from utils.db import db

class User_rol(db.Model):
    __tablename__ = 'user_rol'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), nullable = False)
    str_description = db.Column(db.String(50), nullable = False)

    def __init__(self, description, str_description = description):
       self.description = description
       self.str_description = str_description

    def getId(rol_description):
        return User_rol.query.filter_by(description=rol_description).first().id