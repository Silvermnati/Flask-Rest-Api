from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server import db

appearances_bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@appearances_bp.route('', methods=['POST'])
@jwt_required()
def create_appearance():
    """Create a new appearance (requires authentication)"""
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['rating', 'guest_id', 'episode_id']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Validate rating
    try:
        Appearance.validate_rating(data['rating'])
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    # Check guest exists
    if not Guest.query.get(data['guest_id']):
        return jsonify({'error': 'Guest not found'}), 404
    
    # Check episode exists
    if not Episode.query.get(data['episode_id']):
        return jsonify({'error': 'Episode not found'}), 404
    
    # Create appearance
    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500