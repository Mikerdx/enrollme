from flask import Blueprint, request, jsonify
from models import db, courses

course_bp = Blueprint("course_bp", __name__)

@course_bp.route("/courses", methods=["GET"])
def get_courses():
    courses = courses.query.all()
    return jsonify([{
        "id": course.id,
        "title": course.title,
        "schedule": course.schedule,
        "description": course.description
    } for course in courses]), 200

@course_bp.route("/courses/<int:id>", methods=["GET"])
def get_course(id):
    course = courses.query.get(id)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    return jsonify({
        "id": course.id,
        "title": course.title,
        "schedule": course.schedule,
        "description": course.description
    }), 200

@course_bp.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json()
    title = data.get("title")
    schedule = data.get("schedule")
    description = data.get("description")

    if not title or not schedule or not description:
        return jsonify({"error": "All fields are required"}), 400

    new_course = courses(title=title, schedule=schedule, description=description)
    db.session.add(new_course)
    db.session.commit()

    return jsonify({
        "message": "Course created successfully",
        "course": {
            "id": new_course.id,
            "title": new_course.title,
            "schedule": new_course.schedule,
            "description": new_course.description
        }
    }), 201

@course_bp.route("/courses/<int:id>", methods=["PATCH"])
def update_course(id):
    course = courses.query.get(id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    data = request.get_json()
    course.title = data.get("title", course.title)
    course.schedule = data.get("schedule", course.schedule)
    course.description = data.get("description", course.description)

    db.session.commit()

    return jsonify({
        "message": "Course updated successfully",
        "course": {
            "id": course.id,
            "title": course.title,
            "schedule": course.schedule,
            "description": course.description
        }
    }), 200

@course_bp.route("/courses/<int:id>", methods=["DELETE"])
def delete_course(id):
    course = courses.query.get(id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted successfully"}), 200
