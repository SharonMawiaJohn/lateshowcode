from models import db  # Import db from models, not app

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    appearances = db.relationship('Appearance', backref='episode', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            'appearances': [{'id': appearance.id, 'rating': appearance.rating} for appearance in self.appearances]
        }
