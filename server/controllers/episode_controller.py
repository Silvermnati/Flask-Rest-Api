from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..models.episode import Episode
from ..app import db

episodes_bp = Blueprint("episodes", __name__)

@episodes_bp.route("/episodes", methods=["GET"])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "number": e.number, "date": e.date} for e in episodes])

@episodes_bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [{"guest": a.guest.name, "rating": a.rating} for a in episode.appearances]
    })

@episodes_bp.route("/episodes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message="Episode deleted")
