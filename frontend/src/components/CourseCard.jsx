// src/components/CourseCard.jsx
import { useContext } from "react";
import { UserContext } from "../context/UserContext";

export default function CourseCard({ course, enrolled, onEnroll }) {
  const { currentUser } = useContext(UserContext); // ✅ direct check

  return (
    <div
      className="card h-100 border-0 shadow-sm text-white"
      style={{
        background: "rgba(255, 255, 255, 0.05)",
        backdropFilter: "blur(14px)",
        borderRadius: "1rem",
        transition: "transform 0.3s ease",
      }}
      onMouseEnter={(e) => (e.currentTarget.style.transform = "scale(1.03)")}
      onMouseLeave={(e) => (e.currentTarget.style.transform = "scale(1)")}
    >
      <div className="card-body d-flex flex-column justify-content-between">
        <div>
          <h5 className="fw-semibold mb-2">{course.title}</h5>
          <p className="text-light">Mentor: {course.mentor}</p>
        </div>

        <div className="mt-3">
          {currentUser ? (
            enrolled ? (
              <button className="btn btn-success w-100" disabled>
                ✅ Enrolled
              </button>
            ) : (
              <button
                className="btn btn-outline-light w-100"
                onClick={() => onEnroll(course.id)}
              >
                Enroll
              </button>
            )
          ) : (
            <button
              className="btn btn-outline-secondary w-100"
              disabled
              title="Login to enroll"
            >
              🔒 Login to Enroll
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
