from utils.db import db
from models.productor_type import Productor_type
from flask_bcrypt import generate_password_hash, check_password_hash

class Productor(db.Model) :
    __tablename__ = "productor"
    id = db.Column(db.Integer, primary_key = True)
    cedula = db.Column(db.String(100), nullable = False, unique=True)
    name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    gender = db.Column(db.String(10), nullable = False)
    date_of_birth = db.Column(db.String(10), nullable = False)
    local_phone = db.Column(db.String(20), nullable = True)
    movil_phone = db.Column(db.String(20), nullable = True)
    address_1 = db.Column(db.String(150), nullable = True)
    address_2 = db.Column(db.String(150), nullable = True)
    productor_type_id = db.Column(db.Integer, db.ForeignKey('productor_type.id'))


    def __init__(self, cedula, name, last_name,\
        gender, date_of_birth, local_phone, movil_phone, address_1,\
        address_2, productor_type_description):
        self.cedula = cedula
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.local_phone = local_phone
        self.movil_phone = movil_phone
        self.address_1 = address_1
        self.address_2 = address_2
        self.productor_type_id = Productor_type.getId(description = productor_type_description)

    def __repr__(self):
        return '<Post %r >' % self.id
