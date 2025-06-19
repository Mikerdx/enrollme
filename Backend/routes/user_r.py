from flask import Flask, request, jsonify, Blueprint
from models import db
from models.user import User
from werkzeug.security import generate_password_hash
from flask_mail import Message
from flask import current_app



User_bp = Blueprint("User_bp", __name__)


@User_bp.route("/Users", methods=["POST"])
def create_User():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")


    if not username or not email or not password:
        return jsonify({"error": "Username, email and password are required"}), 400
     
    username_exists = User.query.filter_by(Username=username).first()
    email_exists = User.query.filter_by(email=email).first()

    if username_exists:
        return jsonify({"error": "Username already exists"}), 400

    if email_exists:
        return jsonify({"error": "Email already exists"}), 400
    
    role = data.get("role", "student")
    new_User = User(Username=username, email=email, password = generate_password_hash(password),role=role )
    db.session.add(new_User)

    try:
        msg = Message(subject="Welcome to StackOverflow Clone",
        recipients=[email],
        sender=current_app.config['MAIL_DEFAULT_SENDER'],
        body=f"Hello {username},\n\nThank you for registering on StackOverflow Clone. We are excited to have you on board!\n\nBest regards,\nStackOverflow Clone Team")
        current_app.extensions['mail'].send(msg)       
        db.session.commit()
        return jsonify({"success":"User created successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to regsiter/send welcome email"}), 400

@User_bp.route("/Users/<User_id>", methods=["PATCH"])
def update_User(User_id):  
    user = User.query.get(User_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
  
    username = data.get("username",user.Username)
    email = data.get("email", user.email)
    user.role = data.get("role", user.role)
    is_blocked = data.get("is_blocked", user.is_blocked)

    
    user.Username = username
    user.email = email
    # user.role = role
    user.is_blocked = is_blocked
    
    try:
        msg = Message(subject="Alert! Profile Update",
        recipients=[email],
        sender=current_app.config['MAIL_DEFAULT_SENDER'],
        body=f"Hello {user.Username},\n\nYour Profile has been updated successfully on StackOverflow Clone.\n\nBest regards,\nStackOverflow Clone Team")
        current_app.extensions['mail'].send(msg)       
        db.session.commit()
        return jsonify({"success":"User updated successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to regsiter/send welcome email"}), 400
   


@User_bp.route("/Users/<User_id>", methods=["GET"])
def fetch_User_by_id(User_id):
    User = User.query.get(User_id)

    if not User:
        return jsonify({"error": "User not found"}), 404

    User_data = {
        "id": User.id,
        "Username": User.Username,
        "email": User.email,
        "is_admin": User.is_admin,
        "is_blocked": User.is_blocked,
        "created_at": User.created_at,
    }
    return jsonify(User_data), 200


@User_bp.route("/Users", methods=["GET"])
def fetch_all_Users():
    Users = User.query.all()

    User_list = []
    for User in Users:
        User_data = {
            "id": User.id,
            "Username": User.Username,
            "email": User.email,
            "is_admin": User.is_admin,
            "is_blocked": User.is_blocked,
            "created_at": User.created_at
        }
        User_list.append(User_data)
        
    return jsonify(User_list), 200


@User_bp.route("/Users/<User_id>", methods=["DELETE"])
def delete_User(User_id):
    user = User.query.get(User_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"success": "User deleted successfully"}), 200