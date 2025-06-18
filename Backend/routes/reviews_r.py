from flask import Blueprint, request, jsonify
from models import db, Reviews, Course, User

Reviews_bp = Blueprint("Reviews_bp", __name__)


@Reviews_bp.route("/Reviews", methods=["GET"])
def get_all_Reviews():
    Reviews = Reviews.query.all()
    return jsonify([{
        "id": r.id,
        "content": r.content,
        "rating": r.rating,
        "course_id": r.course_id,
        "User_id": r.User_id
    } for r in Reviews]), 200


@Reviews_bp.route("/Reviews/<int:id>", methods=["GET"])
def get_review(id):
    review = Reviews.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    return jsonify({
        "id": review.id,
        "content": review.content,
        "rating": review.rating,
        "course_id": review.course_id,
        "User_id": review.User_id
    }), 200


@Reviews_bp.route("/Reviews", methods=["POST"])
def create_review():
    data = request.get_json()
    content = data.get("content")
    rating = data.get("rating")
    course_id = data.get("course_id")
    User_id = data.get("User_id")

    if not all([content, rating, course_id, User_id]):
        return jsonify({"error": "All fields are required"}), 400

    course = course.query.get(course_id)
    User = User.query.get(User_id)
    if not course or not User:
        return jsonify({"error": "Invalid course or User ID"}), 404

    new_review = Reviews(content=content, rating=rating, course_id=course_id, User_id=User_id)
    db.session.add(new_review)
    db.session.commit()

    return jsonify({
        "message": "Review created successfully",
        "review": {
            "id": new_review.id,
            "content": new_review.content,
            "rating": new_review.rating,
            "course_id": new_review.course_id,
            "User_id": new_review.User_id
        }
    }), 201


@Reviews_bp.route("/Reviews/<int:id>", methods=["PATCH"])
def update_review(id):
    review = Reviews.query.get(id)
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
            "User_id": review.User_id
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
