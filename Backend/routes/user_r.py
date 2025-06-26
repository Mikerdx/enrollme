from flask import Blueprint, request, jsonify, current_app
from Backend.models import db
from Backend.models.user import User
from werkzeug.security import generate_password_hash
from flask_mail import Message
from flask_jwt_extended import jwt_required, get_jwt_identity
from auth_decorators import admin_required
from flask_cors import cross_origin

User_bp = Blueprint("User_bp", __name__)

@User_bp.route("/Users", methods=["POST"])
@cross_origin(origin="http://127.0.0.1:5173", supports_credentials=True)
def create_user():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Username, email and password are required"}), 400

    if User.query.filter_by(Username=username).first():
        return jsonify({"error": "Username already exists"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    role = data.get("role", "student")
    hashed_password = generate_password_hash(password)
    new_user = User(Username=username, email=email, password=hashed_password, role=role)
    db.session.add(new_user)

    try:
        msg = Message(
            subject="Welcome to Course Enrollment App",
            recipients=[email],
            sender=current_app.config['MAIL_DEFAULT_SENDER'],
            body=f"Hello {username},\n\nThank you for registering on the Course Enrollment App."
        )
        current_app.extensions['mail'].send(msg)
        db.session.commit()
        return jsonify({"success": "User created successfully"}), 201
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to register/send welcome email"}), 400

@User_bp.route("/Users/me", methods=["GET"])
@jwt_required()
def fetch_my_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "Username": user.Username,
        "email": user.email,
        "role": user.role,
        "is_blocked": user.is_blocked,
        "created_at": user.created_at
    }), 200

@User_bp.route("/Users/<int:user_id>", methods=["PATCH"])
@admin_required
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.Username = data.get("username", user.Username)
    user.email = data.get("email", user.email)
    user.role = data.get("role", user.role)
    user.is_blocked = data.get("is_blocked", user.is_blocked)

    try:
        msg = Message(
            subject="Profile Updated",
            recipients=[user.email],
            sender=current_app.config['MAIL_DEFAULT_SENDER'],
            body=f"Hello {user.Username},\n\nYour profile has been updated."
        )
        current_app.extensions['mail'].send(msg)
        db.session.commit()
        return jsonify({"success": "User updated successfully"}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Failed to update/send notification email"}), 400

@User_bp.route("/Users/<int:user_id>", methods=["GET"])
@admin_required
def fetch_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "Username": user.Username,
        "email": user.email,
        "role": user.role,
        "is_blocked": user.is_blocked,
        "created_at": user.created_at
    }), 200

@User_bp.route("/Users", methods=["GET"])
@admin_required
def fetch_all_users():
    users = User.query.all()
    return jsonify([{
        "id": u.id,
        "Username": u.Username,
        "email": u.email,
        "role": u.role,
        "is_blocked": u.is_blocked,
        "created_at": u.created_at
    } for u in users]), 200

@User_bp.route("/Users/<int:user_id>", methods=["DELETE"])
@admin_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"success": "User deleted successfully"}), 200
