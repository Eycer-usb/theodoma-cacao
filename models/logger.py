from utils.db import db
from time import gmtime, strftime

class Logger(db.Model):
    __tablename__ = 'logger'
    id = db.Column( db.Integer, primary_key = True )
    event = db.Column(db.String(50), nullable = False)
    module = db.Column(db.String(50), nullable = False)
    date = db.Column( db.Date, nullable=False, default= strftime("%Y-%m-%d", gmtime() ) )
    time = db.Column( db.String(20), nullable=False, default= strftime("%H:%M:%S", gmtime() ) )

    def __init__(self, event, user, module, date, time):
        self.event = event
        self.module = module
        self.date = date
        self.time = time

    def getId(event):
        return Logger.query.filter_by(event=event).first().id