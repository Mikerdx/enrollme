// src/pages/Dashboard.jsx
import React, { useState } from "react";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import StudentDashboard from "./StudentDashboard";
import MentorDashboard from "./MentorDashboard";
import AdminDashboard from "./AdminDashboard";

export default function Dashboard() {
  const [darkMode, setDarkMode] = useState(true);
  const role = "student"; 

  const background = darkMode
    ? "linear-gradient(135deg, #0f172a, #1e293b)"
    : "linear-gradient(135deg, #e0f2fe, #fef9c3)";

  return (
    <div
      className="d-flex"
      style={{
        height: "100vh",
        background,
        color: darkMode ? "#fff" : "#1e293b",
        transition: "all 0.4s ease",
        overflow: "hidden",
      }}
    >
      <Sidebar role={role} darkMode={darkMode} />
      <div className="flex-grow-1 d-flex flex-column">
        <Topbar role={role} darkMode={darkMode} setDarkMode={setDarkMode} />

        <div className="p-5" style={{ overflowY: "auto" }}>
          {/* Load role-specific dashboard */}
          {role === "student" && <StudentDashboard />}
          {role === "mentor" && <MentorDashboard />}
          {role === "admin" && <AdminDashboard />}
          {/* Future: Add MentorDashboard / AdminDashboard here */}
        </div>
      </div>
    </div>
  );
}
