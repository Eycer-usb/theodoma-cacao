"""
This class hold the productor-type data
A productor-type has its description and id
"""


from utils.db import db

class Productor_type(db.Model):
    # Initial class Atributes
    __tablename__ = 'productor_type'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), nullable = False)
    price_percentage = db.Column( db.Float, nullable = False )

    # Class Constructor
    def __init__(self, description, price_percentage):
        self.description = description
        self.price_percentage = price_percentage


    # Given a productor type description, when is call return 
    # its id
    def getId(description):
        return Productor_type.query.filter_by(description=description).first().id

