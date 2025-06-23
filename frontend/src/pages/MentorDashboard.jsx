// src/pages/MentorDashboard.jsx
import React, { useState } from "react";

export default function MentorDashboard() {
  const [courses, setCourses] = useState([]);
  const [formData, setFormData] = useState({
    title: "",
    description: "",
  });

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newCourse = {
      id: Date.now(),
      ...formData,
    };
    setCourses((prev) => [...prev, newCourse]);
    setFormData({ title: "", description: "" });
  };

  return (
    <div className="container py-4">
      <h3 className="fw-bold mb-4">👨‍🏫 Mentor Dashboard</h3>

      <div className="card shadow-sm mb-4">
        <div className="card-body">
          <h5 className="card-title">Create New Course</h5>
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">Course Title</label>
              <input
                type="text"
                className="form-control"
                name="title"
                value={formData.title}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Description</label>
              <textarea
                className="form-control"
                name="description"
                value={formData.description}
                onChange={handleChange}
                required
              />
            </div>
            <button className="btn btn-primary" type="submit">
              Add Course
            </button>
          </form>
        </div>
      </div>

      <h5 className="mb-3">📚 My Courses</h5>
      {courses.length === 0 ? (
        <p className="text-muted">You haven’t created any courses yet.</p>
      ) : (
        <ul className="list-group">
          {courses.map((course) => (
            <li key={course.id} className="list-group-item">
              <strong>{course.title}</strong> <br />
              <small className="text-muted">{course.description}</small>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
