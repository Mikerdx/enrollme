from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import MetaData

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
class user():
     __tablename__ = 'users'
     
     id = db.column(db.integer, primary_key = True)
     username = db.column(db.string(255), nullable = False, unique = True)
     email = db.column(db.string(255), nullable = False, unique = True)
     password = db.column(db.varchar(8), nullable = False)
     role = db.column(db.string(10), nullable = False)
     created_at = db.column(db.Datetime, default = datetime.utcnow)
     
     profile = db.relationship('profile', backref='user', uselist=False)
     courses = db.relationship('course', backref='mentor', lazy=True, foreign_keys='course.mentor_id')
     enrollments = db.relationship('enrollment', backref='student', lazy=True, foreign_keys='Enrollment.student_id')
     reviews = db.relationship('review', backref='user', lazy=True)