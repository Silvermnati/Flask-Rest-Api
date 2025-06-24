from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server import db
from datetime import datetime

episodes_bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@episodes_bp.route('', methods=['GET'])
def get_episodes():
    """Get all episodes"""
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

@episodes_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    """Get a specific episode with appearances"""
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict()), 200

@episodes_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    """Delete an episode (requires authentication)"""
    episode = Episode.query.get_or_404(id)
    
    try:
        db.session.delete(episode)
        db.session.commit()
        return jsonify({'message': 'Episode deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500