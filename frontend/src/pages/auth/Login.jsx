import React, { useContext, useState } from "react";
import { UserContext } from "../../context/UserContext";
import { Link, useNavigate } from "react-router-dom";

const Login = () => {
  const { login_user } = useContext(UserContext);
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: ""
  });

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const { email, password } = formData;
    const res = await login_user(email, password);

    if (res) {
      navigate("/dashboard"); // ✅ redirect from here
    }
  };

  return (
    <div className="min-vh-100 d-flex justify-content-center align-items-center bg-light px-4">
      <div className="w-100" style={{ maxWidth: "400px" }}>
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-center text-primary mb-4">Login to Your Account</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            <input
              type="email"
              name="email"
              placeholder="Email"
              required
              value={formData.email}
              onChange={handleChange}
              className="form-control mb-3"
            />
            <input
              type="password"
              name="password"
              placeholder="Password"
              required
              value={formData.password}
              onChange={handleChange}
              className="form-control mb-3"
            />
            <button type="submit" className="btn btn-primary w-100">
              Login
            </button>
          </form>
          <p className="text-center mt-3">
            Don't have an account?{" "}
            <Link to="/register" className="text-decoration-none text-primary">
              Register
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
