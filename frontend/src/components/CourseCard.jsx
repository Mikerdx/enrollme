import React, { useContext, useState, useEffect } from "react";
import { UserContext } from "../context/UserContext";
import CourseCard from "../components/CourseCard";
import { toast } from "react-toastify";

export default function Courses() {
  const { authToken, currentUser } = useContext(UserContext);
  const [courses, setCourses] = useState([]);
  const [enrollments, setEnrollments] = useState([]);
  const baseURL = import.meta.env.VITE_API_BASE_URL;

  useEffect(() => {
    fetch(`${baseURL}/Course`, {
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then(res => res.json())
      .then(data => setCourses(Array.isArray(data) ? data : []));
  }, [authToken, baseURL]);

  useEffect(() => {
    fetch(`${baseURL}/Enrollments`, {
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then(res => res.json())
      .then(data => {
        if (Array.isArray(data)) {
          setEnrollments(
            data.filter(e => e.student_id === currentUser?.id).map(e => e.course_id)
          );
        }
      });
  }, [authToken, currentUser, baseURL]);

  const handleEnroll = (courseId) => {
    fetch(`${baseURL}/Enrollments`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${authToken}`,
      },
      body: JSON.stringify({ course_id: courseId }),
    })
      .then(res => res.json())
      .then(data => {
        if (data.error) toast.error(data.error);
        else {
          toast.success("Enrolled successfully!");
          setEnrollments(prev => [...prev, courseId]);
        }
      })
      .catch(() => toast.error("Enrollment failed"));
  };

  return (
    <div className="row">
      {courses.map(course => (
        <div className="col-md-4 mb-4" key={course.id}>
          <CourseCard
            course={course}
            enrolled={enrollments.includes(course.id)}
            onEnroll={handleEnroll}
          />
        </div>
      ))}
    </div>
  );
}
