from flask import Blueprint, request, jsonify
from models import db, Profile, User

Profile_bp = Blueprint("Profile_bp", __name__)

@Profile_bp.route("/Profiles", methods=["GET"])
def get_Profiles():
    profiles = Profile.query.all()
    return jsonify([{
        "id": p.id,
        "bio": p.bio,
        "avatar_url": p.avatar_url,
        "User_id": p.User_id,
        "created_at": p.created_at
    } for p in profiles]), 200

@Profile_bp.route("/Profiles/<int:id>", methods=["GET"])
def get_Profile(id):
    profile = Profile.query.get(id)
    if not profile:
        return jsonify({"error": "Profile not found"}), 404

    return jsonify({
        "id": profile.id,
        "bio": profile.bio,
        "avatar_url": profile.avatar_url,
        "User_id": profile.User_id,
        "created_at": profile.created_at
    }), 200

@Profile_bp.route("/Profiles", methods=["POST"])
def create_Profile():
    data = request.get_json()
    bio = data.get("bio")
    avatar_url = data.get("avatar_url")
    User_id = data.get("User_id")

    if not User_id:
        return jsonify({"error": "User_id is required"}), 400

    user = User.query.get(User_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    profile = Profile(bio=bio, avatar_url=avatar_url, User_id=User_id)
    db.session.add(profile)
    db.session.commit()

    return jsonify({"message": "Profile created", "Profile_id": profile.id}), 201

@Profile_bp.route("/Profiles/<int:id>", methods=["PATCH"])
def update_Profile(id):
    profile = Profile.query.get(id)
    if not profile:
        return jsonify({"error": "Profile not found"}), 404

    data = request.get_json()
    profile.bio = data.get("bio", profile.bio)
    profile.avatar_url = data.get("avatar_url", profile.avatar_url)

    db.session.commit()
    return jsonify({"message": "Profile updated"}), 200

@Profile_bp.route("/Profiles/<int:id>", methods=["DELETE"])
def delete_Profile(id):
    profile = Profile.query.get(id)
    if not profile:
        return jsonify({"error": "Profile not found"}), 404

    db.session.delete(profile)
    db.session.commit()
    return jsonify({"message": "Profile deleted"}), 200
