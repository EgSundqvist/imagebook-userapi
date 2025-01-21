from db import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    bio = db.Column(db.String(500), nullable=True)
    avatar = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Profile {self.username}>'