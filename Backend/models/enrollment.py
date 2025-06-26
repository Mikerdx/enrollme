from Backend.models.user import db
from datetime import datetime
from sqlalchemy import UniqueConstraint

class Enrollment(db.Model):
    __tablename__ = 'Enrollments'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    progress = db.Column(db.Float, default=0.0)
    status = db.Column(db.String, default="Awaiting Approval")
    approved_by = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    admin = db.relationship("User", backref="approved_Enrollments", foreign_keys=[approved_by])

    __table_args__ = (
        UniqueConstraint('student_id', 'course_id', name='uq_student_course'),
    )
