// src/pages/StudentDashboard.jsx
import React, { useState } from "react";
import CourseCard from "../components/CourseCard";

const dummyCourses = [
  { id: 1, title: "Intro to Web Dev", mentor: "Alex Kariuki" },
  { id: 2, title: "Python for Data Science", mentor: "Fatuma Ali" },
  { id: 3, title: "Machine Learning Basics", mentor: "J. Kim" },
];

const enrolled = [1]; // dummy enrolled course IDs

export default function StudentDashboard() {
  const [courses, setCourses] = useState(dummyCourses);
  const [enrollments, setEnrollments] = useState(enrolled);

  const handleEnroll = (id) => {
    if (!enrollments.includes(id)) {
      setEnrollments([...enrollments, id]);
    }
  };

  return (
    <div className="container py-4">
      <h3 className="fw-bold mb-4">📚 Available Courses</h3>
      <div className="row g-4">
        {courses.map((course) => (
          <div key={course.id} className="col-md-4">
            <CourseCard
              course={course}
              enrolled={enrollments.includes(course.id)}
              onEnroll={handleEnroll}
            />
          </div>
        ))}
      </div>

      <hr className="my-5" />

      <h4 className="mb-3">✅ My Enrollments</h4>
      <ul className="list-group">
        {courses
          .filter((c) => enrollments.includes(c.id))
          .map((course) => (
            <li key={course.id} className="list-group-item">
              {course.title} — <em>{course.mentor}</em>
            </li>
          ))}
        {enrollments.length === 0 && (
          <li className="list-group-item text-muted">No courses enrolled yet.</li>
        )}
      </ul>
    </div>
  );
}
