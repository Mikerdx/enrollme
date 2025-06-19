from flask import Blueprint, request, jsonify, current_app
from models import db
from models.user import User
from werkzeug.security import generate_password_hash
from flask_mail import Message

User_bp = Blueprint("User_bp", __name__)

@User_bp.route("/Users", methods=["POST"])
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
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to register/send welcome email"}), 400

@User_bp.route("/Users/<int:user_id>", methods=["PATCH"])
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
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update/send notification email"}), 400

@User_bp.route("/Users/<int:user_id>", methods=["GET"])
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
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"success": "User deleted successfully"}), 200
