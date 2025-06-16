from datetime import timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_jwt_extended import JWTManager


from models import db,courses,enrollment,profile,reviews,user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'kelvinapp2025@gmail.com'
app.config['MAIL_PASSWORD'] = 'rvkh mymz ttzx rrqb'
app.config['MAIL_DEFAULT_SENDER'] = 'kelvinapp2025@gmail.com'

app.config['JWT_SECRET_KEY'] = 'sjusefvyilgfvksbhvfiknhalvufn'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)

db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)
jwt = JWTManager(app)

@app.route("/")
def index():
    return "<h1>Course Enrollment App is running!</h1>"

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    new_user = user(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
