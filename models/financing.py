"""
Purchase Entity.

Any Collector can buy from harvests. It keep
the purchase data and details
"""

from utils.db import db


class Financing( db.Model ):

    # Purchase Attributes
    __tablename__ = 'financing'
    id = db.Column( db.Integer, primary_key = True )
    date = db.Column( db.String(10), nullable = False )
    F_Productor = db.Column( db.Integer, db.ForeignKey('productor.id'))
    F_Harvest = db.Column( db.Integer, db.ForeignKey( 'harvest.id' ) )
    letter_number = db.Column( db.Integer, nullable = False )
    expiration_date = db.Column( db.String(10), nullable = False )
    amount = db.Column( db.Float, nullable = False )
    payment = db.Column(db.String(10), nullable = False )
    observations = db.Column( db.String(100), nullable = False )

    #Class Constuctor
    def __init__( self, date, F_Productor, F_Harvest, letter_number,
                expiration_date, amount, payment, observations):
        self.date = date
        self.F_Productor = F_Productor
        self.F_Harvest = F_Harvest
        self.letter_number = letter_number
        self.expiration_date = expiration_date
        self.amount = amount
        self.payment = payment
        self.observations = observations

    # Return the register with given Id
    def find(self, id):
        return Purchase.query.get(id)