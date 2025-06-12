from .user import db
from datetime import datetime
class profile():
     __tablename__ = 'profiles'
     id = db.Column(db.Integer, primary_key = True)
     bio = db.Column(db.Text)
     avatar_url = db.Column(db.String(255))
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique = True)
     created_at = db.Column(db.DateTime, default = datetime.utcnow)
     updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)