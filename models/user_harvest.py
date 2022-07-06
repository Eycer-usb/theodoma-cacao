from utils.db import db

class User_harvest(db.Model):
    # Initial class Atributes
    __tablename__ = 'user_harvest'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), nullable = False)
    start_date = db.Column(db.String(10), nullable = False)
    ended_date = db.Column(db.String(10), nullable = False)


    # Class Constructor
    def __init__(self, description, start_date, ended_date):
        self.description = description
        self.start_date = start_date
        self.ended_date = ended_date

    def getId(description):
        return User_harvest.query.filter_by(description=description).first().id

