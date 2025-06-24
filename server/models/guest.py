from server import db

class Guest(db.Model):
    """Guest model for late show guests"""
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    
    # Relationship to appearances (one-to-many)
    appearances = db.relationship('Appearance', backref='guest', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Guest {self.name}, {self.occupation}>'
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }