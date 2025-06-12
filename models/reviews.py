from .user import db
from datetime import datetime
class reviews():
     __tablename__ = 'reviews'
     id = db.column(db.integer, primary_key = True)
     student_id = db.column(db.integer, db.ForeignKey('users.id'), nullable = False, unique = True)
     course_id = db.column(db.integer, db.ForeignKey('courses.id'), nullable = False, unique = True)
     rating = db.column(db.integer, nullable = True)
     review = db.column(db.text)
     created_at = db.column(db.Datetime, default = datetime.utcnow)
     