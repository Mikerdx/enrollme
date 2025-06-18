from flask import Blueprint, request, jsonify
from models import db, Profile, User

Profile_bp = Blueprint("Profile_bp", __name__)


@Profile_bp.route("/Profiles", methods=["GET"])
def get_Profiles():
    Profiles = Profile.query.all()
    return jsonify([{
        "id": p.id,
        "bio": p.bio,
        "location": p.location,
        "User_id": p.User_id
    } for p in Profiles]), 200


@Profile_bp.route("/Profiles/<int:id>", methods=["GET"])
def get_Profile(id):
    Profile = Profile.query.get(id)
    if not Profile:
        return jsonify({"error": "Profile not found"}), 404

    return jsonify({
        "id": Profile.id,
        "bio": Profile.bio,
        "location": Profile.location,
        "User_id": Profile.User_id
    }), 200


@Profile_bp.route("/Profiles", methods=["POST"])
def create_Profile():
    data = request.get_json()
    bio = data.get("bio")
    location = data.get("location")
    User_id = data.get("User_id")

    if not User_id:
        return jsonify({"error": "User_id is required"}), 400

    User = User.query.get(User_id)
    if not User:
        return jsonify({"error": "User not found"}), 404

    Profile = Profile(bio=bio, location=location, User_id=User_id)
    db.session.add(Profile)
    db.session.commit()

    return jsonify({"message": "Profile created", "Profile_id": Profile.id}), 201


@Profile_bp.route("/Profiles/<int:id>", methods=["PATCH"])
def update_Profile(id):
    Profile = Profile.query.get(id)
    if not Profile:
        return jsonify({"error": "Profile not found"}), 404

    data = request.get_json()
    Profile.bio = data.get("bio", Profile.bio)
    Profile.location = data.get("location", Profile.location)

    db.session.commit()
    return jsonify({"message": "Profile updated"}), 200

@Profile_bp.route("/Profiles/<int:id>", methods=["DELETE"])
def delete_Profile(id):
    Profile = Profile.query.get(id)
    if not Profile:
        return jsonify({"error": "Profile not found"}), 404

    db.session.delete(Profile)
    db.session.commit()
    return jsonify({"message": "Profile deleted"}), 200
