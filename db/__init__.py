from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models import User, Profile

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


