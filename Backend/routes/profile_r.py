from flask import Blueprint, request, jsonify
from Backend.models import db, Profile, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from Backend.auth_decorators import admin_required

Profile_bp = Blueprint("Profile_bp", __name__)

@Profile_bp.route("/Profiles", methods=["GET"])
@admin_required
def get_Profiles():
    profiles = Profile.query.all()
    return jsonify([{
        "id": p.id,
        "bio": p.bio,
        "avatar_url": p.avatar_url,
        "User_id": p.User_id,
        "created_at": p.created_at
    } for p in profiles]), 200

@Profile_bp.route("/Profiles/me", methods=["GET"])
@jwt_required()
def get_Profile():
    user_id = get_jwt_identity()
    profile = Profile.query.filter_by(User_id=user_id).first()
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
@jwt_required()
def create_Profile():
    user_id = get_jwt_identity()
    if Profile.query.filter_by(User_id=user_id).first():
        return jsonify({"error": "Profile already exists"}), 400

    data = request.get_json()
    bio = data.get("bio")
    avatar_url = data.get("avatar_url")

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    profile = Profile(bio=bio, avatar_url=avatar_url, User_id=user_id)
    db.session.add(profile)
    db.session.commit()

    return jsonify({"message": "Profile created", "Profile_id": profile.id}), 201

@Profile_bp.route("/Profiles/me", methods=["PATCH"])
@jwt_required()
def update_Profile():
    user_id = get_jwt_identity()
    profile = Profile.query.filter_by(User_id=user_id).first()
    if not profile:
        return jsonify({"error": "Profile not found"}), 404

    data = request.get_json()
    profile.bio = data.get("bio", profile.bio)
    profile.avatar_url = data.get("avatar_url", profile.avatar_url)

    db.session.commit()
    return jsonify({
        "id": profile.id,
        "bio": profile.bio,
        "avatar_url": profile.avatar_url,
        "User_id": profile.User_id,
        "created_at": profile.created_at
    }), 200

@Profile_bp.route("/Profiles/me", methods=["DELETE"])
@jwt_required()
def delete_Profile():
    user_id = get_jwt_identity()
    profile = Profile.query.filter_by(User_id=user_id).first()
    if not profile:
        return jsonify({"error": "Profile not found"}), 404

    db.session.delete(profile)
    db.session.commit()
    return jsonify({"message": "Profile deleted"}), 200
