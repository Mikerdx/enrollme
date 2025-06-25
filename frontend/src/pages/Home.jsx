import React from "react";
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div
      className="min-vh-100 d-flex align-items-center"
      style={{
        background: "radial-gradient(circle at center, #1e293b, #0f172a)",
        color: "#f1f5f9",
        overflow: "hidden",
      }}
    >
      <div className="container text-center py-5">
        <h1
          className="fw-bold display-3 mb-4"
          style={{
            background: "linear-gradient(90deg, #38bdf8, #9333ea)",
            WebkitBackgroundClip: "text",
            WebkitTextFillColor: "transparent",
          }}
        >
          Welcome to EnrollMe 🚀
        </h1>
        <p
          className="lead mb-5"
          style={{ color: "#cbd5e1", maxWidth: "600px", margin: "0 auto" }}
        >
          EnrollMe is your one-stop learning platform for courses across web
          development, data science, AI, and more. Empower your future — today.
        </p>

        <div className="d-flex flex-column flex-sm-row justify-content-center gap-3">
          <Link to="/login" className="btn btn-primary btn-lg px-5">
            Login
          </Link>
          <Link to="/register" className="btn btn-outline-light btn-lg px-5">
            Get Started
          </Link>
        </div>
      </div>
    </div>
  );
}
