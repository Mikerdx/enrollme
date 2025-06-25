import React from "react";

export default function Topbar({ role, darkMode, setDarkMode }) {
  return (
    <div
      className="d-flex justify-content-between align-items-center px-4 py-3"
      style={{
        backgroundColor: darkMode
          ? "rgba(255,255,255,0.05)"
          : "rgba(255,255,255,0.7)",
        backdropFilter: "blur(10px)",
        borderBottom: "1px solid rgba(0,0,0,0.1)",
      }}
    >
      <h5 className="m-0">Dashboard</h5>
      <div className="d-flex align-items-center gap-3">
        <span className="badge bg-primary text-capitalize">{role}</span>
        <button
          className={`btn btn-sm ${
            darkMode ? "btn-outline-light" : "btn-outline-dark"
          }`}
          onClick={() => setDarkMode(!darkMode)}
        >
          {darkMode ? "🌙" : "☀️"}
        </button>
      </div>
    </div>
  );
}
