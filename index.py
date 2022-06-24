"""
Start Gateway

And app instance is created and the service start
running in debug mode
"""

from app import create_app
from utils.db import db

if __name__ == '__main__':
    app = create_app()  
    with app.app_context():
        db.create_all()
    app.run(debug=True)