from .user import db
from datetime import datetime

class Course(db.Model):
    __tablename__ = 'courses' 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
     
    Enrollments = db.relationship('Enrollment', backref = 'Course', lazy = True)
    Reviews = db.relationship ('Reviews', backref = 'Course', lazy = True)
     
    def __repr__(self):
        return f"<Course {self.title}>"
