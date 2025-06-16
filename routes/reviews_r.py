from flask import Blueprint, request, jsonify
from models import db, reviews, courses, user

reviews_bp = Blueprint("reviews_bp", __name__)


@reviews_bp.route("/reviews", methods=["GET"])
def get_all_reviews():
    reviews = reviews.query.all()
    return jsonify([{
        "id": r.id,
        "content": r.content,
        "rating": r.rating,
        "course_id": r.course_id,
        "user_id": r.user_id
    } for r in reviews]), 200


@reviews_bp.route("/reviews/<int:id>", methods=["GET"])
def get_review(id):
    review = reviews.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    return jsonify({
        "id": review.id,
        "content": review.content,
        "rating": review.rating,
        "course_id": review.course_id,
        "user_id": review.user_id
    }), 200


@reviews_bp.route("/reviews", methods=["POST"])
def create_review():
    data = request.get_json()
    content = data.get("content")
    rating = data.get("rating")
    course_id = data.get("course_id")
    user_id = data.get("user_id")

    if not all([content, rating, course_id, user_id]):
        return jsonify({"error": "All fields are required"}), 400

    course = course.query.get(course_id)
    user = user.query.get(user_id)
    if not course or not user:
        return jsonify({"error": "Invalid course or user ID"}), 404

    new_review = reviews(content=content, rating=rating, course_id=course_id, user_id=user_id)
    db.session.add(new_review)
    db.session.commit()

    return jsonify({
        "message": "Review created successfully",
        "review": {
            "id": new_review.id,
            "content": new_review.content,
            "rating": new_review.rating,
            "course_id": new_review.course_id,
            "user_id": new_review.user_id
        }
    }), 201


@reviews_bp.route("/reviews/<int:id>", methods=["PATCH"])
def update_review(id):
    review = reviews.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    data = request.get_json()
    review.content = data.get("content", review.content)
    review.rating = data.get("rating", review.rating)

    db.session.commit()

    return jsonify({
        "message": "Review updated successfully",
        "review": {
            "id": review.id,
            "content": review.content,
            "rating": review.rating,
            "course_id": review.course_id,
            "user_id": review.user_id
        }
    }), 200


@reviews_bp.route("/reviews/<int:id>", methods=["DELETE"])
def delete_review(id):
    review = reviews.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    db.session.delete(review)
    db.session.commit()

    return jsonify({"message": "Review deleted successfully"}), 200
