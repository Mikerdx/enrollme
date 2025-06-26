from Backend.models.user import db
from datetime import datetime

class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)