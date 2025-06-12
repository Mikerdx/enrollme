from .user import db
from datetime import datetime
class profile():
     __tablename__ = 'profiles'
     id = db.column(db.integer, primary_key = True)
     bio = db.column(db.text)
     avatar_url = db.column(db.string(255))
     user_id = db.column(db.integer, db.ForeignKey('users.id'),unique = True)
     created_at = db.column(db.Datetime, default = datetime.utcnow)
     updated_at = db.column(db.datetime, default = datetime.utcnow, onupdate = datetime.utcnow)