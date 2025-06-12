from .user import db
from datetime import datetime

class courses():
     __tablename__ = 'courses'
     
     id = db.column(db.integer, primary_key = True)
     title = db.column(db.string(255), nullable = False, unique = True)
     description = db.column(db.text(255), nullable = False)
     mentor_id = db.column(db.integer, db.ForeignKey('users.id'), nullable = False, unique = True)
     created_at = db.column(db.Datetime, default = datetime.utcnow)
     updated_at = db.column(db.datetime, default = datetime.utcnow, onupdate = datetime.utcnow)
     
     enrollments = db.relationship('enrollment', backref = 'course', Lazy = True)
     reviews = db.relationship ('reviews', backref = 'course', Lazy = True)
