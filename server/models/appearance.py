from server import db

class Appearance(db.Model):
    """Appearance model for guests appearing on episodes"""
    __tablename__ = 'appearances'
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    
    def __repr__(self):
        return f'<Appearance {self.id}, Rating: {self.rating}>'
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'rating': self.rating,
            'guest': self.guest.to_dict(),
            'episode_id': self.episode_id
        }
    
    @staticmethod
    def validate_rating(rating):
        """Validate that rating is between 1 and 5"""
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError('Rating must be an integer between 1 and 5')