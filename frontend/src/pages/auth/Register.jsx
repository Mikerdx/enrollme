import React, { useState, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { Link } from "react-router-dom";

const Register = () => {
  const { register_user } = useContext(UserContext);

  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const { username, email, password } = formData;
    register_user(username, email, password);
  };

  return (
    <div className="min-vh-100 d-flex justify-content-center align-items-center bg-light px-3">
      <div className="card shadow-sm p-4 w-100" style={{ maxWidth: "400px" }}>
        <h2 className="text-center text-primary mb-4">Create Account</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <input
              type="text"
              name="username"
              placeholder="Username"
              required
              value={formData.username}
              onChange={handleChange}
              className="form-control"
            />
          </div>
          <div className="mb-3">
            <input
              type="email"
              name="email"
              placeholder="Email"
              required
              value={formData.email}
              onChange={handleChange}
              className="form-control"
            />
          </div>
          <div className="mb-4">
            <input
              type="password"
              name="password"
              placeholder="Password"
              required
              value={formData.password}
              onChange={handleChange}
              className="form-control"
            />
          </div>
          <button type="submit" className="btn btn-primary w-100">
            Register
          </button>
        </form>
        <p className="mt-3 text-center text-muted">
          Already have an account?{" "}
          <Link to="/login" className="text-decoration-none text-primary fw-bold">
            Login
          </Link>
        </p>
      </div>
    </div>
  );
};

export default Register;
