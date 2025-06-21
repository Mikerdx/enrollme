// src/components/Navbar.jsx
import React, { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";

const Navbar = () => {
  const { currentUser, logout_user } = useContext(UserContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout_user();
    navigate("/login");
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
      <div className="container">
        <Link className="navbar-brand" to="/">CourseApp</Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
            {!currentUser && (
              <>
                <li className="nav-item">
                  <Link className="nav-link" to="/login">Login</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/register">Register</Link>
                </li>
              </>
            )}

            {currentUser && (
              <>
                <li className="nav-item">
                  <Link className="nav-link" to="/dashboard">Dashboard</Link>
                </li>

                {currentUser.role === "admin" && (
                  <li className="nav-item">
                    <Link className="nav-link" to="/admin/users">Manage Users</Link>
                  </li>
                )}

                {currentUser.role === "mentor" && (
                  <li className="nav-item">
                    <Link className="nav-link" to="/mentor/courses">My Courses</Link>
                  </li>
                )}

                {currentUser.role === "student" && (
                  <li className="nav-item">
                    <Link className="nav-link" to="/courses">Enroll</Link>
                  </li>
                )}

                <li className="nav-item">
                  <Link className="nav-link" to="/profile">Profile</Link>
                </li>
                <li className="nav-item">
                  <button
                    className="btn btn-outline-light btn-sm ms-2"
                    onClick={handleLogout}
                  >
                    Logout
                  </button>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
