// src/components/Footer.jsx
import React from "react";

const Footer = () => {
  return (
    <footer className="bg-primary text-white py-4 mt-auto">
      <div className="container text-center">
        <p className="mb-0">&copy; {new Date().getFullYear()} CourseApp. All rights reserved.</p>
        <small className="d-block">Empowering education through smart enrollment.</small>
      </div>
    </footer>
  );
};

export default Footer;
