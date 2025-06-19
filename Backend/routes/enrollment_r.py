from flask import Blueprint, request, jsonify
from models import db, Enrollment, Course, User

Enrollment_bp = Blueprint("Enrollment_bp", __name__)

@Enrollment_bp.route("/Enrollments", methods=["GET"])
def get_Enrollments():
    enrollments = Enrollment.query.all()
    return jsonify([{
        "id": e.id,
        "course_id": e.course_id,
        "student_id": e.student_id,
        "approved_by": e.approved_by,
        "progress": e.progress,
        "status": e.status,
        "created_at": e.created_at
    } for e in enrollments]), 200

@Enrollment_bp.route("/Enrollments", methods=["POST"])
def enroll_User():
    data = request.get_json()
    course_id = data.get("course_id")
    student_id = data.get("student_id")
    approved_by = data.get("approved_by")

    if not all([course_id, student_id, approved_by]):
        return jsonify({"error": "course_id, student_id, and approved_by are required"}), 400

    course = Course.query.get(course_id)
    student = User.query.get(student_id)
    admin = User.query.get(approved_by)

    if not course or not student or not admin:
        return jsonify({"error": "Course, student, or approving admin not found"}), 404

    new_enrollment = Enrollment(course_id=course_id, student_id=student_id, approved_by=approved_by)
    db.session.add(new_enrollment)
    db.session.commit()

    return jsonify({"message": "User enrolled successfully", "Enrollment_id": new_enrollment.id}), 201

@Enrollment_bp.route("/Enrollments/<int:id>", methods=["DELETE"])
def delete_Enrollment(id):
    enrollment = Enrollment.query.get(id)
    if not enrollment:
        return jsonify({"error": "Enrollment not found"}), 404

    db.session.delete(enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment deleted successfully"}), 200
