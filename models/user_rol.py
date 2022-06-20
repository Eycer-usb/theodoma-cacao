from utils.db import db

class User_rol(db.Model):
    __tablename__ = 'user_rol'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), nullable = False)
    #user = db.relationship("User", back_populates="user_rol")

    def __init__(self, description):
       self.description = description

    def getId(rol_description):
        return User_rol.query.filter_by(description=rol_description).first().id