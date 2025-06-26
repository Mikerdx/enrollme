import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

from datetime import timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from models import db
from models.user import TokenBlocklist
from routes.courses_r import course_bp
from routes.reviews_r import Reviews_bp
from routes.enrollment_r import Enrollment_bp
from routes.profile_r import Profile_bp
from routes.mentor_r import mentor_bp
from routes.user_r import User_bp
from flask_cors import CORS
from auth_decorators import admin_required, mentor_required, student_required


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mman73942@gmail.com'
app.config['MAIL_PASSWORD'] = 'flhk jhao patw tgbn'
app.config['MAIL_DEFAULT_SENDER'] = 'mman73942@gmail.com'

app.config['JWT_SECRET_KEY'] = 'sjusefvyilgfvksbhvfiknhalvufn'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=200)
app.config["JWT_VERIFY_SUB"] = False


CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5173"}}, supports_credentials=True)
db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)
jwt = JWTManager(app)

@app.route("/")
def index():
    return "<h1>Course Enrollment App is running!</h1>"

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(course_bp)
app.register_blueprint(Reviews_bp)
app.register_blueprint(Enrollment_bp)
app.register_blueprint(Profile_bp)
app.register_blueprint(User_bp)
app.register_blueprint(mentor_bp)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
