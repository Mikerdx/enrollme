from flask import Blueprint, request, jsonify
from models import db, Enrollment, Course, User

Enrollment_bp = Blueprint("Enrollment_bp", __name__)


@Enrollment_bp.route("/Enrollments", methods=["GET"])
def get_Enrollments():
    Enrollments = Enrollment.query.all()
    return jsonify([{
        "id": e.id,
        "course_id": e.course_id,
        "User_id": e.User_id,
        "approved_by": e.approved_by
    } for e in Enrollments]), 200


@Enrollment_bp.route("/Enrollments", methods=["POST"])
def enroll_User():
    data = request.get_json()
    course_id = data.get("course_id")
    User_id = data.get("User_id")
    approved_by = data.get("approved_by")  

    if not all([course_id, User_id, approved_by]):
        return jsonify({"error": "course_id, User_id, and approved_by are required"}), 400

    course = Course.query.get(course_id)
    User = User.query.get(User_id)

    if not course or not User:
        return jsonify({"error": "Course or User not found"}), 404

    new_Enrollment = Enrollment(course_id=course_id, User_id=User_id, approved_by=approved_by)
    db.session.add(new_Enrollment)
    db.session.commit()

    return jsonify({"message": "User enrolled successfully", "Enrollment_id": new_Enrollment.id}), 201

# 
@Enrollment_bp.route("/Enrollments/<int:id>", methods=["DELETE"])
def delete_Enrollment(id):
    Enrollment = Enrollment.query.get(id)
    if not Enrollment:
        return jsonify({"error": "Enrollment not found"}), 404

    db.session.delete(Enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment deleted successfully"}), 200
