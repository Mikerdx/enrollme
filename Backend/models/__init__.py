from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import user
from .courses import courses
from .enrollment import enrollment
from .profile import profile
from .reviews import reviews
