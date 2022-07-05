"""
Harvest class representation

A Harvest linked with a date range

"""


from utils.db import db

class Harvest (db.Model):

    # Harvest Attributtes 
    __tablename__ = 'harvest'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(250), nullable = False)
    start_date = db.Column(db.String(10), nullable=False)
    end_date = db.Column(db.String(10), nullable= False)
    status = db.Column(db.String(10), nullable = False)

    # Class constructor
    def __init__(self, id, description, start_date, end_date, status):
        self.id = id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    # Given a Id return the harvest if exist
    def find(self, id):
        return Harvest.query.get(id)
