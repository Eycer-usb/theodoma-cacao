"""
Purchase Entity.

Any Collector can buy from harvests. It keep
the purchase data and details
"""

from utils.db import db


class Purchase( db.Model ):

    # Purchase Attributes
    __tablename__ = 'purchase'
    id = db.Column( db.Integer, primary_key = True )
    F_Productor = db.Column( db.Integer, db.ForeignKey('productor.id'))
    F_Harvest = db.Column( db.Integer, db.ForeignKey( 'harvest.id' ) )
    date = db.Column( db.String(10), nullable = False )
    cacao_type = db.Column( db.String, nullable=False )
    price_dolar= db.Column( db.Float, nullable=False )
    amount_dolar = db.Column( db.Float, nullable = False )
    wetness_percentage = db.Column( db.Float, nullable = False )
    waste_percentage = db.Column( db.Float, nullable = False )
    waste_kg = db.Column( db.Float, nullable=False )
    total_amont_kg = db.Column( db.Float )
    total_dolar = db.Column( db.Float )
    observation = db. Column( db.String(255) )

    #Class Constuctor
    def __init__( self, date, F_Productor, 
                F_Harvest, cacao_type, price_dolar,
                amount_dolar, wetness_percentage,
                waste_percentage, waste_kg, total_amont_kg,
                total_dolar, observation):

        self.date = date
        self.F_Productor = F_Productor
        self.F_Harvest = F_Harvest
        self.cacao_type = cacao_type
        self.price_dolar = price_dolar
        self.amount_dolar = amount_dolar
        self.wetness_percentage = wetness_percentage
        self.waste_percentage = waste_percentage
        self.waste_kg = waste_kg
        self.total_amont_kg = total_amont_kg
        self.total_dolar = total_dolar
        self.observation = observation

    # Return the register with given Id
    def find(self, id):
        return Purchase.query.get(id)