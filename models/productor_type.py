from utils.db import db

class Productor_type(db.Model):
    __tablename__ = 'productor_type'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), nullable = False)

    def __init__(self, description):
       self.description = description

    def getId(description):
        return Productor_type.query.filter_by(description=description).first().id