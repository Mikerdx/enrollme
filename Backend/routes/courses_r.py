from flask import Blueprint, request, jsonify
from models import db, Course

course_bp = Blueprint("course_bp", __name__)

@course_bp.route("/Course", methods=["GET"])
def get_Course():
    courses = Course.query.all()
    return jsonify([{
        "id": course.id,
        "title": course.title,
        "description": course.description
    } for course in courses]), 200

@course_bp.route("/Course/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get(id)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    return jsonify({
        "id": course.id,
        "title": course.title,
        "description": course.description
    }), 200

@course_bp.route("/Course", methods=["POST"])
def create_course():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    mentor_id = data.get("mentor_id")

    if not title or not description or not mentor_id:
        return jsonify({"error": "All fields are required"}), 400

    new_course = Course(title=title, description=description, mentor_id=mentor_id)
    db.session.add(new_course)
    db.session.commit()

    return jsonify({
        "message": "Course created successfully",
        "course": {
            "id": new_course.id,
            "title": new_course.title,
            "description": new_course.description,
            "mentor_id": new_course.mentor_id
        }
    }), 201

@course_bp.route("/Course/<int:id>", methods=["PATCH"])
def update_course(id):
    course = Course.query.get(id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    data = request.get_json()
    course.title = data.get("title", course.title)
    course.description = data.get("description", course.description)
    db.session.commit()

    return jsonify({
        "message": "Course updated successfully",
        "course": {
            "id": course.id,
            "title": course.title,
            "description": course.description
        }
    }), 200

@course_bp.route("/Course/<int:id>", methods=["DELETE"])
def delete_course(id):
    course = Course.query.get(id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted successfully"}), 200
