from flask import Blueprint, request, jsonify
from models import db, profile, user

profile_bp = Blueprint("profile_bp", __name__)


@profile_bp.route("/profiles", methods=["GET"])
def get_profiles():
    profiles = profile.query.all()
    return jsonify([{
        "id": p.id,
        "bio": p.bio,
        "location": p.location,
        "user_id": p.user_id
    } for p in profiles]), 200


@profile_bp.route("/profiles/<int:id>", methods=["GET"])
def get_profile(id):
    profile = profile.query.get(id)
    if not profile:
        return jsonify({"error": "Profile not found"}), 404

    return jsonify({
        "id": profile.id,
        "bio": profile.bio,
        "location": profile.location,
        "user_id": profile.user_id
    }), 200


@profile_bp.route("/profiles", methods=["POST"])
def create_profile():
    data = request.get_json()
    bio = data.get("bio")
    location = data.get("location")
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    user = user.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    profile = profile(bio=bio, location=location, user_id=user_id)
    db.session.add(profile)
    db.session.commit()

    return jsonify({"message": "Profile created", "profile_id": profile.id}), 201


@profile_bp.route("/profiles/<int:id>", methods=["PATCH"])
def update_profile(id):
    profile = profile.query.get(id)
    if not profile:
        return jsonify({"error": "Profile not found"}), 404

    data = request.get_json()
    profile.bio = data.get("bio", profile.bio)
    profile.location = data.get("location", profile.location)

    db.session.commit()
    return jsonify({"message": "Profile updated"}), 200

@profile_bp.route("/profiles/<int:id>", methods=["DELETE"])
def delete_profile(id):
    profile = profile.query.get(id)
    if not profile:
        return jsonify({"error": "Profile not found"}), 404

    db.session.delete(profile)
    db.session.commit()
    return jsonify({"message": "Profile deleted"}), 200
