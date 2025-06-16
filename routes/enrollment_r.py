from flask import Blueprint, request, jsonify
from models import db, enrollment, courses, user

enrollment_bp = Blueprint("enrollment_bp", __name__)


@enrollment_bp.route("/enrollments", methods=["GET"])
def get_enrollments():
    enrollments = enrollment.query.all()
    return jsonify([{
        "id": e.id,
        "course_id": e.course_id,
        "user_id": e.user_id,
        "approved_by": e.approved_by
    } for e in enrollments]), 200


@enrollment_bp.route("/enrollments", methods=["POST"])
def enroll_user():
    data = request.get_json()
    course_id = data.get("course_id")
    user_id = data.get("user_id")
    approved_by = data.get("approved_by")  

    if not all([course_id, user_id, approved_by]):
        return jsonify({"error": "course_id, user_id, and approved_by are required"}), 400

    course = courses.query.get(course_id)
    user = user.query.get(user_id)

    if not course or not user:
        return jsonify({"error": "Course or User not found"}), 404

    new_enrollment = enrollment(course_id=course_id, user_id=user_id, approved_by=approved_by)
    db.session.add(new_enrollment)
    db.session.commit()

    return jsonify({"message": "User enrolled successfully", "enrollment_id": new_enrollment.id}), 201

# 
@enrollment_bp.route("/enrollments/<int:id>", methods=["DELETE"])
def delete_enrollment(id):
    enrollment = enrollment.query.get(id)
    if not enrollment:
        return jsonify({"error": "Enrollment not found"}), 404

    db.session.delete(enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment deleted successfully"}), 200
