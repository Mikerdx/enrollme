from flask import request, jsonify, Blueprint
from Backend.models import db, User, TokenBlocklist
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from datetime import datetime, timezone
from flask_cors import cross_origin

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login", methods=["POST"])
@cross_origin(origin="http://127.0.0.1:5173", supports_credentials=True)
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    if not email or not password:
        return jsonify({"error": "email and password are required to login"}), 400

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.Username,
                "email": user.email,
                "role": user.role
            }
        }), 200
    else:
        return jsonify({"error": "User does not exist or wrong credentials"}), 400

@auth_bp.route("/current_User", methods=["GET"])
@jwt_required()
def fetch_current_User():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    user_data = {
        "id": user.id,
        "Username": user.Username,
        "email": user.email,
        "role": user.role,
        "is_blocked": user.is_blocked,
        "created_at": user.created_at
    }
    return jsonify(user_data), 200

@auth_bp.route("/logout", methods=["DELETE"])
@jwt_required()
def modify_token():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    new_blocked_token = TokenBlocklist(jti=jti, created_at=now)
    db.session.add(new_blocked_token)
    db.session.commit()
    return jsonify({"success": "Successfully logged out"}), 200
