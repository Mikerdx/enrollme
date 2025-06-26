from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from Backend.models.user import User,TokenBlocklist

from Backend.models.user import User
from Backend.models.user import TokenBlocklist
from Backend.models.courses import Course
from Backend.models.enrollment import Enrollment
from Backend.models.profile import Profile
from Backend.models.reviews import Reviews
from Backend.models.user import db  
