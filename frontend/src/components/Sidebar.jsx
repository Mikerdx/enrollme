// src/components/Sidebar.jsx
import React, { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";

export default function Sidebar({ role, darkMode }) {
  const { logout_user } = useContext(UserContext);
  const navigate = useNavigate();

  const bg = darkMode
    ? "rgba(30,41,59,0.6)"
    : "rgba(255,255,255,0.6)";

  const linkColor = darkMode ? "text-white" : "text-dark";

  return (
    <div
      className="p-4 shadow-lg d-flex flex-column justify-content-between"
      style={{
        width: "240px",
        height: "100vh",
        backdropFilter: "blur(12px)",
        backgroundColor: bg,
        color: darkMode ? "#fff" : "#1e293b",
        borderRight: "1px solid rgba(255,255,255,0.1)",
        transition: "all 0.4s ease",
      }}
    >
      <div>
        <h4 className="fw-bold mb-4 text-center">EnrollMe</h4>
        <ul className="nav flex-column">
          <li className="nav-item mb-2">
            <Link to="/dashboard" className={`nav-link fw-semibold ${linkColor}`}>
              🏠 Dashboard
            </Link>
          </li>
          <li className="nav-item mb-2">
            <Link to="/profile" className={`nav-link fw-semibold ${linkColor}`}>
              👤 Profile
            </Link>
          </li>
          <li className="nav-item mb-2">
            <Link to="/courses" className={`nav-link fw-semibold ${linkColor}`}>
              📚 Courses
            </Link>
          </li>
          {role === "admin" && (
            <li className="nav-item mb-2">
              <Link to="/users" className={`nav-link fw-semibold ${linkColor}`}>
                👥 Manage Users
              </Link>
            </li>
          )}
        </ul>
      </div>

      <button
        className={`btn ${darkMode ? "btn-outline-light" : "btn-outline-dark"} w-100 mt-4`}
        onClick={() => {
          logout_user();
          navigate("/login");
        }}
      >
        🔓 Logout
      </button>
    </div>
  );
}
