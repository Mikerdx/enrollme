from .user import db
from datetime import datetime

class courses():
     __tablename__ = 'courses'
     
     id = db.Column(db.Integer, primary_key = True)
     title = db.Column(db.String(255), nullable = False, unique = True)
     description = db.Column(db.Text(255), nullable = False)
     mentor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False, unique = True)
     created_at = db.Column(db.DateTime, default = datetime.utcnow)
     updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
     
     enrollments = db.relationship('enrollment', backref = 'course', Lazy = True)
     reviews = db.relationship ('reviews', backref = 'course', Lazy = True)
