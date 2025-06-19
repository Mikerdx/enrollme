from flask import Blueprint, request, jsonify
from models import db, Reviews, Course, User

Reviews_bp = Blueprint("Reviews_bp", __name__)

@Reviews_bp.route("/Reviews", methods=["GET"])
def get_all_reviews():
    reviews = Reviews.query.all()
    return jsonify([{
        "id": r.id,
        "review": r.review,
        "rating": r.rating,
        "course_id": r.course_id,
        "student_id": r.student_id,
        "created_at": r.created_at
    } for r in reviews]), 200

@Reviews_bp.route("/Reviews/<int:id>", methods=["GET"])
def get_review(id):
    review = Reviews.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    return jsonify({
        "id": review.id,
        "review": review.review,
        "rating": review.rating,
        "course_id": review.course_id,
        "student_id": review.student_id,
        "created_at": review.created_at
    }), 200

@Reviews_bp.route("/Reviews", methods=["POST"])
def create_review():
    data = request.get_json()
    review_text = data.get("review")
    rating = data.get("rating")
    course_id = data.get("course_id")
    student_id = data.get("student_id")

    if not all([review_text, rating, course_id, student_id]):
        return jsonify({"error": "All fields are required"}), 400

    course = Course.query.get(course_id)
    student = User.query.get(student_id)
    if not course or not student:
        return jsonify({"error": "Invalid course or student ID"}), 404

    new_review = Reviews(review=review_text, rating=rating, course_id=course_id, student_id=student_id)
    db.session.add(new_review)
    db.session.commit()

    return jsonify({
        "message": "Review created successfully",
        "review": {
            "id": new_review.id,
            "review": new_review.review,
            "rating": new_review.rating,
            "course_id": new_review.course_id,
            "student_id": new_review.student_id,
            "created_at": new_review.created_at
        }
    }), 201

@Reviews_bp.route("/Reviews/<int:id>", methods=["PATCH"])
def update_review(id):
    review = Reviews.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    data = request.get_json()
    review.review = data.get("review", review.review)
    review.rating = data.get("rating", review.rating)

    db.session.commit()

    return jsonify({
        "message": "Review updated successfully",
        "review": {
            "id": review.id,
            "review": review.review,
            "rating": review.rating,
            "course_id": review.course_id,
            "student_id": review.student_id,
            "created_at": review.created_at
        }
    }), 200

@Reviews_bp.route("/Reviews/<int:id>", methods=["DELETE"])
def delete_review(id):
    review = Reviews.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    db.session.delete(review)
    db.session.commit()

    return jsonify({"message": "Review deleted successfully"}), 200
