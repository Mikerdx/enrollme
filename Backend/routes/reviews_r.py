from flask import Blueprint, request, jsonify
from Backend.models import db, Reviews, Course, User
from Backend.auth_decorators import student_required
from flask_jwt_extended import jwt_required, get_jwt_identity

Reviews_bp = Blueprint("Reviews_bp", __name__)

@Reviews_bp.route("/Reviews", methods=["GET"])
@jwt_required()
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
@jwt_required()
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
@student_required
def create_review():
    data = request.get_json()
    review_text = data.get("review")
    rating = data.get("rating")
    course_id = data.get("course_id")
    student_id = get_jwt_identity()

    if not all([review_text, rating, course_id]):
        return jsonify({"error": "All fields are required"}), 400

    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": "Invalid course ID"}), 404

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
@student_required
def update_review(id):
    review = Reviews.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    student_id = get_jwt_identity()
    if review.student_id != student_id:
        return jsonify({"error": "You can only edit your own review"}), 403

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
@student_required
def delete_review(id):
    review = Reviews.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    student_id = get_jwt_identity()
    if review.student_id != student_id:
        return jsonify({"error": "You can only delete your own review"}), 403

    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted successfully"}), 200
