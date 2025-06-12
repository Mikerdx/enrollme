from .user import db 
from datetime import datetime
class enrollment():
     __tablename__ = 'enrollments'
     
     id = db.Column(db.Integer, primary_key = True)
     student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False, unique = True)
     course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable = False, unique = True)
     progress = db.Column(db.float, default = 0.0)
     status = db.Column(db.String, default = "Awaiting Approval")
     approved_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
     created_at = db.Column(db.DateTime, default = datetime.utcnow)
     
     admin = db.relationship('user',db.Foreign_Keys[approved_by])