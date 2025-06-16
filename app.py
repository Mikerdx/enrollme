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
from routes.reviews_r import reviews_bp
from routes.enrollment_r import enrollment_bp
from routes.profile_r import profile_bp


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'manmike@gmail.com'
app.config['MAIL_PASSWORD'] = '45719370m'
app.config['MAIL_DEFAULT_SENDER'] = 'manmike@gmail.com'


app.config['JWT_SECRET_KEY'] = 'sjusefvyilgfvksbhvfiknhalvufn'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)
app.config["JWT_VERIFY_SUB"] = False

db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)
jwt = JWTManager(app)
jwt.init_app(app)

@app.route("/")
def index():
    return "<h1>Course Enrollment App is running!</h1>"


app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(course_bp)
app.register_blueprint(reviews_bp)
app.register_blueprint(enrollment_bp)
app.register_blueprint(profile_bp)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None

if __name__ == "__main__":
    app.run(debug=True)
