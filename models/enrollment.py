from .user import db 
from datetime import datetime
class enrollment():
     __tablename__ = 'enrollments'
     
     id = db.column(db.integer, primary_key = True)
     student_id = db.column(db.integer, db.ForeignKey('users.id'), nullable = False, unique = True)
     course_id = db.column(db.integer, db.ForeignKey('courses.id'), nullable = False, unique = True)
     progress = db.column(db.float, default = 0.0)
     status = db.column(db.string, default = "Awaiting Approval")
     approved_by = db.column(db.integer, db.ForeignKey('users.id'), nullable = False)
     created_at = db.column(db.Datetime, default = datetime.utcnow)
     
     admin = db.relationship('user',db.Foreign_Keys[approved_by])