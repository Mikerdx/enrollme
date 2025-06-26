import React, { useState, useEffect, useContext } from "react";
import CourseCard from "../components/CourseCard";
import { UserContext } from "../context/UserContext";
import { toast } from "react-toastify";

export default function Courses() {
  const { authToken, currentUser, loading } = useContext(UserContext);
  const [courses, setCourses] = useState([]);
  const [enrollments, setEnrollments] = useState([]);
  const baseURL = import.meta.env.VITE_API_BASE_URL;

  useEffect(() => {
    fetch(`${baseURL}/Course`, {
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) setCourses(data);
        else setCourses([]);
      })
      .catch(() => setCourses([]));
  }, [authToken, baseURL]);

  useEffect(() => {
    if (!authToken) return;
    fetch(`${baseURL}/Enrollments`, {
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setEnrollments(
            data
              .filter((e) => e.student_id === currentUser?.id)
              .map((e) => e.course_id)
          );
        }
      })
      .catch(() => {});
  }, [authToken, currentUser, baseURL]);

  if (loading) return <div>Loading courses...</div>;

  const handleEnroll = (courseId) => {
    if (!authToken) {
      toast.error("You must be logged in to enroll.");
      return;
    }
    fetch(`${baseURL}/Enrollments`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${authToken}`,
      },
      body: JSON.stringify({ course_id: courseId }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) toast.error(data.error);
        else {
          toast.success("Enrolled successfully!");
          setEnrollments((prev) => [...prev, courseId]);
        }
      })
      .catch(() => toast.error("Enrollment failed"));
  };

  return (
    <div
      className="min-vh-100 py-5"
      style={{
        background: "radial-gradient(circle at top left, #0f172a, #1e293b)",
        color: "#f1f5f9",
        overflowX: "hidden",
      }}
    >
      <div className="container text-center">
        <h2
          className="fw-bold mb-3 display-5"
          style={{
            background: "linear-gradient(90deg, #3b82f6, #ec4899)",
            WebkitBackgroundClip: "text",
            WebkitTextFillColor: "transparent",
          }}
        >
          🚀 Explore Our Courses
        </h2>
        <p
          className="mb-5"
          style={{
            color: "#94a3b8",
            maxWidth: "600px",
            margin: "0 auto",
          }}
        >
          Browse our expert-curated collection and start learning today.
        </p>

        <div className="row g-4">
          {courses.length === 0 ? (
            <div className="col-12 text-muted">No available courses.</div>
          ) : (
            courses.map((course) => (
              <div key={course.id} className="col-sm-12 col-md-6 col-lg-4">
                <CourseCard
                  course={course}
                  enrolled={enrollments.includes(course.id)}
                  onEnroll={handleEnroll}
                />
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
