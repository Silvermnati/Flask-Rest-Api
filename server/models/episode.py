from server import db
from datetime import datetime

class Episode(db.Model):
    """Episode model for late show episodes"""
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    
    # Relationship to appearances (one-to-many)
    appearances = db.relationship('Appearance', backref='episode', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Episode {self.number}, {self.date}>'
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'number': self.number,
            'appearances': [appearance.to_dict() for appearance in self.appearances]
        }