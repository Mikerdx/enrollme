from .user import db
from datetime import datetime
class reviews():
     __tablename__ = 'reviews'
     id = db.Column(db.Integer, primary_key = True)
     student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False, unique = True)
     course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable = False, unique = True)
     rating = db.Column(db.Integer, nullable = True)
     review = db.Column(db.Text)
     created_at = db.Column(db.DateTime, default = datetime.utcnow)
     