// src/pages/student/CourseDetails.jsx
import React from "react";
import { useParams } from "react-router-dom";

const CourseDetails = () => {
  const { id } = useParams();

  return (
    <div className="container py-5">
      <h1>Course Details</h1>
      <p>Course ID: {id}</p>
    </div>
  );
};

export default CourseDetails;
