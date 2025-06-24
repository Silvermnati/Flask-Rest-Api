from flask import Blueprint, request, jsonify
from server.models.guest import Guest
from server import db

guests_bp = Blueprint('guests', __name__, url_prefix='/guests')

@guests_bp.route('', methods=['GET'])
def get_guests():
    """Get all guests"""
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200