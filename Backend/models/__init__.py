from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User,TokenBlocklist

from .user import User
from .user import TokenBlocklist
from .courses import Course
from .enrollment import Enrollment
from .profile import Profile
from .reviews import Reviews
from .user import db  
