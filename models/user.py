from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import MetaData

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
class user(db.Model):
     __tablename__ = 'users'
     
     id = db.Column(db.Integer, primary_key = True)
     username = db.Column(db.String(255), nullable = False, unique = True)
     email = db.Column(db.String(255), nullable = False, unique = True)
     password = db.Column(db.String(8), nullable = False)
     role = db.Column(db.String(10), nullable = False)
     created_at = db.Column(db.DateTime, default = datetime.utcnow)
     
     profile = db.relationship('profile', backref='user', uselist=False)
     courses = db.relationship('course', backref='mentor', lazy=True, foreign_keys='course.mentor_id')
     enrollments = db.relationship('enrollment', backref='student', lazy=True, foreign_keys='Enrollment.student_id')
     reviews = db.relationship('review', backref='user', lazy=True)