import os
from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from flask_cors import CORS

load_dotenv()


from Backend.routes.auth import auth_bp
from Backend.routes.courses_r import course_bp
from Backend.routes.reviews_r import Reviews_bp
from Backend.routes.enrollment_r import Enrollment_bp
from Backend.routes.profile_r import Profile_bp
from Backend.routes.mentor_r import mentor_bp
from Backend.routes.user_r import User_bp

from Backend.models import db
from Backend.models.user import TokenBlocklist

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=200)
app.config["JWT_VERIFY_SUB"] = False


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

(CORS(app, resources={r"/*": {"origins": "https://enrollme-kzvozbgmg-mikes-projects-47769368.vercel.app"}}, supports_credentials=True))

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
