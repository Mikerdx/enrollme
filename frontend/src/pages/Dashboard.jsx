import React, { useState, useContext } from "react";
import Topbar from "../components/Topbar";
import StudentDashboard from "./StudentDashboard";
import MentorDashboard from "./MentorDashboard";
import AdminDashboard from "./AdminDashboard";
import { UserContext } from "../context/UserContext";

export default function Dashboard() {
  const [darkMode, setDarkMode] = useState(true);
  const { user } = useContext(UserContext);
  const role = user?.role || "student"; 

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
      <div className="flex-grow-1 d-flex flex-column">
        <Topbar role={role} darkMode={darkMode} setDarkMode={setDarkMode} />

        <div className="p-5" style={{ overflowY: "auto" }}>
          {role === "student" && <StudentDashboard />}
          {role === "mentor" && <MentorDashboard />}
          {role === "admin" && <AdminDashboard />}
        </div>
      </div>
    </div>
  );
}
