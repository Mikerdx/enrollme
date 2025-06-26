import React, { useState, useEffect, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { toast } from "react-toastify";

export default function MentorDashboard() {
  const { authToken, user } = useContext(UserContext);
  const [courses, setCourses] = useState([]);
  const [formData, setFormData] = useState({
    title: "",
    description: "",
  });

  const baseURL = import.meta.env.VITE_API_BASE_URL;

  useEffect(() => {
    if (!authToken) return;
    fetch(`${baseURL}/Course/my`, {
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then((res) => res.json())
      .then((data) => setCourses(data))
      .catch(() => toast.error("Failed to fetch courses"));
  }, [authToken, baseURL]);

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.title || !formData.description) {
      toast.error("Please fill in all fields.");
      return;
    }
    if (!authToken) {
      toast.error("You are not authenticated.");
      return;
    }

    const payload = {
      ...formData,
      mentor_id: user?.id,
    };

    fetch(`${baseURL}/Course`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${authToken}`,
      },
      body: JSON.stringify(payload),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) {
          toast.error(data.error);
        } else {
          toast.success("Course added!");
          setCourses((prev) => [...prev, data]);
          setFormData({ title: "", description: "" });
        }
      })
      .catch(() => toast.error("Failed to add course"));
  };

  const handleDelete = (courseId) => {
    if (!window.confirm("Are you sure you want to delete this course?")) return;

    fetch(`${baseURL}/Course/${courseId}`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) toast.error(data.error);
        else {
          toast.success("Course deleted!");
          setCourses((prev) => prev.filter((c) => c.id !== courseId));
        }
      })
      .catch(() => toast.error("Failed to delete course"));
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
            <li key={course.id} className="list-group-item d-flex justify-content-between align-items-center">
              <div>
                <strong>{course.title}</strong> <br />
                <small className="text-muted">{course.description}</small>
              </div>
              <button
                className="btn btn-sm btn-danger"
                onClick={() => handleDelete(course.id)}
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
