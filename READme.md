# Course Enrollment System

This is a full-stack Course Enrollment System built with a Flask REST API backend and a React frontend. The system includes authentication with JWT, role-based access control (admin, student, mentor), and functionality for managing users, courses, and enrollments.

## Features

- User registration and login
- JWT authentication
- Admin can create, update, delete courses and enrollments
- Students can enroll in courses
- Mentors can view assigned courses (optional)
- React frontend with role-based routing and UI
- Deployed with Render (backend) and Vercel (frontend)

---

## Project Structure

course-enrollment-system/
├── Backend/                     
│   ├── app.py                      
│   ├── auth_decorators.py        
│   ├── instance/                   
│   ├── migrations/                
│   ├── models/                    
│   │   ├── __init__.py
│   │   ├── courses.py
│   │   ├── enrollment.py
│   │   ├── profile.py
│   │   ├── reviews.py
│   │   └── user.py
│   └── routes/             
│       └── __init__.py             

├── frontend/                  
│   ├── public/                    
│   ├── src/
│   │   ├── assets/            
│   │   ├── components/            
│   │   ├── context/               
│   │   │   ├── UserContext.jsx
│   │   │   └── ProtectedRoutes.jsx
│   │   ├── pages/                  
│   │   │   ├── AdminDashboard.jsx
│   │   │   ├── MentorDashboard.jsx
│   │   │   ├── StudentDashboard.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Courses.jsx
│   │   │   ├── ProfilePage.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Login.jsx
│   │   │   └── Home.jsx
│   │   ├── App.jsx                 
│   │   ├── main.jsx                
│   │   ├── App.css                
│   │   └── index.css              
│   ├── .env                        
│   ├── .gitignore
│   ├── index.html
│   └── eslint.config.js

├── README.md                        
├── LICENSE                          
└── .gitignore


---

## Backend Setup (Flask)

### Local Development

1. Navigate to the backend directory:

```bash
cd Backend
Create virtual environment and install dependencies:

pipenv install
pipenv shell
Create a .env file with the following content:

FLASK_APP=app.py
FLASK_ENV=production
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=8TUEfPAVVlENt1kPmYED9xA4l0J8JQfQmRVFCzUdV39RSr7IBJfCEW_fmrpDHeLbIvfXqWkOwDNZTcZGZrEk3A
MAIL_USERNAME=mman73942@gmail.com
MAIL_PASSWORD=flhk jhao patw tgbn
MAIL_DEFAULT_SENDER=mman73942@gmail.com
PORT=5000

Initialize and migrate the database:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Start the backend server:

flask run
Deployment on Render
Push your code to GitHub
Go to https://render.com and click "New Web Service"
Connect your repo and choose:
Runtime: Python 3.11.9

Start command: gunicorn Backend.app:app

Add environment variables:

FLASK_APP=app.py
FLASK_ENV=production
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=8TUEfPAVVlENt1kPmYED9xA4l0J8JQfQmRVFCzUdV39RSr7IBJfCEW_fmrpDHeLbIvfXqWkOwDNZTcZGZrEk3A
MAIL_USERNAME=mman73942@gmail.com
MAIL_PASSWORD=flhk jhao patw tgbn
MAIL_DEFAULT_SENDER=mman73942@gmail.com
Deploy and copy the backend URL 

Frontend Setup (React)
Local Development
Navigate to the frontend directory:

cd frontend
Install dependencies:

npm install
Configure the backend URL in .env:

VITE_API_BASE_URL=https://enrollme-3.onrender.com
Start the development server:
npm run dev
Deployment on Vercel
Push  repo to GitHub

Go to https://vercel.com and click "New Project"
Select the repo and set:
Framework Preset: Vite
Build Command: npm run build
Output Directory: dist
Add environment variable:

VITE_API_BASE_URL=https://enrollme-3.onrender.com
Click Deploy

API Endpoints
Method	Endpoint	Description
POST	/Users	Register a new user
POST	/auth/login	Log in and receive JWT
GET	/Users/me	Get current user info
POST	/courses	Create a course 
POST	/enrollments	Enroll student
GET	/courses	View all courses

Available Roles
admin,student,mentor
Environment Variables
Backend:
FLASK_APP=app.py
FLASK_ENV=production
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=8TUEfPAVVlENt1kPmYED9xA4l0J8JQfQmRVFCzUdV39RSr7IBJfCEW_fmrpDHeLbIvfXqWkOwDNZTcZGZrEk3A
MAIL_USERNAME=mman73942@gmail.com
MAIL_PASSWORD=flhk jhao patw tgbn
MAIL_DEFAULT_SENDER=mman73942@gmail.com

VITE_API_BASE_URL=https://enrollme-3.onrender.
Video_link=c:\Users\HP\Documents\Zoom\2025-06-27 15.17.25 Mike Bett's Zoom Meeting\video2927098226.mp4

License
MIT License

Copyright (c) 2025 Mike

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

