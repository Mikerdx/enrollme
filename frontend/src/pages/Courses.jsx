// src/pages/Courses.jsx
import React, { useState, useContext } from "react";
import CourseCard from "../components/CourseCard";
import { UserContext } from "../context/UserContext";

const dummyCourses = [
  { id: 1, title: "Full-Stack Web Dev", mentor: "Fatuma Ali" },
  { id: 2, title: "Intro to Python", mentor: "Alex Kariuki" },
  { id: 3, title: "React & API Integration", mentor: "J. Kim" },
  { id: 4, title: "Data Structures", mentor: "Mike Bett" },
  { id: 5, title: "ML Basics", mentor: "Njeri Mwangi" },
];

export default function Courses() {
  const { currentUser, loading } = useContext(UserContext);
  const [enrollments, setEnrollments] = useState([]);

  if (loading) return <div>Loading courses...</div>;

  const isLoggedIn = !!currentUser;

  const handleEnroll = (id) => {
    if (!enrollments.includes(id)) {
      setEnrollments([...enrollments, id]);
    }
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
          {dummyCourses.map((course) => (
            <div key={course.id} className="col-sm-12 col-md-6 col-lg-4">
              <CourseCard
                course={course}
                enrolled={enrollments.includes(course.id)}
                onEnroll={isLoggedIn ? handleEnroll : null}
                isLoggedIn={isLoggedIn} // <-- Pass this!
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
