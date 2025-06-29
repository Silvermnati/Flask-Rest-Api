from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models.appearance import Appearance
from ..app import db

appearance_bp = Blueprint("appearances", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    new = Appearance(
        rating=data["rating"],
        guest_id=data["guest_id"],
        episode_id=data["episode_id"]
    )
    db.session.add(new)
    db.session.commit()
    return jsonify(message="Appearance created"), 201
