from utils.db import db
from time import gmtime, strftime

class Bank(db.Model):
    __tablename__ = 'bank'
    id = db.Column( db.Integer, primary_key = True )
    amountCredit = db. Column( db.Float, nullable = False )
    date = db.Column( db.String(10), nullable = False )
    time = db.Column( db.String(20), nullable = False )
    description = db.Column(db.String(50), nullable = False)
    amount = db. Column( db.Float, nullable = False )

    def __init__(self, amountCredit, date, time, description, amount):
        self.amountCredit = amountCredit
        self.date = date
        self.time = time
        self.description = description
        self.amount = amount


    def find(self, id):
        return Bank.query.get(id)
        
