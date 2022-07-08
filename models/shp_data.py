from utils.db import db
from models.productor_type import Productor_type
from models.productor import Productor
 
class Shopping_data(db.Model):
    # Initial class Atributes
    __tablename__ = 'shp_data'
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(10), nullable = True)
    cedula = db.Column(db.String(100), nullable = True)
    tipo_productor = db.Column(db.Integer, db.ForeignKey('productor_type.id'))
    clase= db.Column(db.String(50), nullable = True)
    price = db.Column(db.String(50), nullable = True)
    cant= db.Column(db.String(50), nullable = True)
    humed= db.Column(db.String(50), nullable = True)
    merma= db.Column(db.String(50), nullable = True)
    mermakg= db.Column(db.String(50), nullable = True)
    cantot= db.Column(db.String(50), nullable = True)
    monto= db.Column(db.String(50), nullable = True)


    # Class Constructor
    def __init__(self, fecha, cedula, tip_productor, clase,\
     price, cant, humed, merma, mermakg, cantot, monto):
        self.fecha = fecha
        self.cedula = cedula
        self.tipo_productor = Productor_type.getId(description = tip_productor)
        self.clase = clase
        self.price = price
        self.cant = cant
        self.humed = humed
        self.merma = merma
        self.mermakg = mermakg
        self.cantot = cantot
        self.monto = monto
        

            # Return the user rol given the username
    def get_shopping_by_cedula( self, cedula ):
        tipo_productor = Productor.query.filter_by(cedula = cedula).first().tipo_productor
        tipos_productor = Productor_type.query.get(tipo_productor).description
        return tipos_productor


"""    def getId(shop_description):
        return Shopping_data.query.filter_by(description=shop_description).first().id"""