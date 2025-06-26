from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from Backend.models import db, Course, User
from Backend.auth_decorators import mentor_required

mentor_bp = Blueprint("mentor_bp", __name__)

@mentor_bp.route("/mentor/courses", methods=["GET"])
@mentor_required
def mentor_view_courses():
    mentor_id = get_jwt_identity()
    courses = Course.query.filter_by(mentor_id=mentor_id).all()
    return jsonify([{ 
        "id": c.id,
        "title": c.title,
        "description": c.description
    } for c in courses]), 200

@mentor_bp.route("/mentor/courses", methods=["POST"])
@mentor_required
def mentor_create_course():
    mentor_id = get_jwt_identity()
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")

    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400

    course = Course(title=title, description=description, mentor_id=mentor_id)
    db.session.add(course)
    db.session.commit()

    return jsonify({
        "message": "Course created successfully",
        "course": {
            "id": course.id,
            "title": course.title,
            "description": course.description
        }
    }), 201

@mentor_bp.route("/mentor/courses/<int:id>", methods=["PATCH"])
@mentor_required
def mentor_update_course(id):
    mentor_id = get_jwt_identity()
    course = Course.query.filter_by(id=id, mentor_id=mentor_id).first()
    if not course:
        return jsonify({"error": "Course not found or not owned by mentor"}), 404

    data = request.get_json()
    course.title = data.get("title", course.title)
    course.description = data.get("description", course.description)
    db.session.commit()

    return jsonify({"message": "Course updated successfully"}), 200

@mentor_bp.route("/mentor/courses/<int:id>", methods=["DELETE"])
@mentor_required
def mentor_delete_course(id):
    mentor_id = get_jwt_identity()
    course = Course.query.filter_by(id=id, mentor_id=mentor_id).first()
    if not course:
        return jsonify({"error": "Course not found or not owned by mentor"}), 404

    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course deleted successfully"}), 200