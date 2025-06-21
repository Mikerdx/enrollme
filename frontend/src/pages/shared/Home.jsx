import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { UserContext } from "../../context/UserContext";

const Home = () => {
  const { currentUser } = useContext(UserContext);

  return (
    <div className="min-vh-100 vw-100 d-flex flex-column justify-content-center align-items-center text-center bg-light p-4">
      <h1 className="display-4 text-primary fw-bold mb-3">
        Welcome to Course Enrollment App
      </h1>
      <p className="lead text-secondary mb-4 px-3">
        Discover, enroll, and review courses easily. Built for admins, mentors, and students.
      </p>

      {!currentUser ? (
        <div className="d-flex gap-3 flex-wrap justify-content-center">
          <Link to="/login" className="btn btn-primary px-4 py-2 fw-semibold">
            Login
          </Link>
          <Link to="/register" className="btn btn-outline-primary px-4 py-2 fw-semibold">
            Register
          </Link>
        </div>
      ) : (
        <div className="d-flex flex-column align-items-center gap-3">
          <p className="h5 text-dark">Welcome back, {currentUser.Username}!</p>

          {currentUser.role === "admin" && (
            <Link to="/admin/dashboard" className="btn btn-success fw-semibold px-4 py-2">
              Admin Dashboard
            </Link>
          )}
          {currentUser.role === "mentor" && (
            <Link to="/mentor/courses" className="btn btn-secondary fw-semibold px-4 py-2">
              My Courses
            </Link>
          )}
          {currentUser.role === "student" && (
            <Link to="/courses" className="btn btn-info fw-semibold px-4 py-2 text-white">
              Browse Courses
            </Link>
          )}
        </div>
      )}
    </div>
  );
};

export default Home;
