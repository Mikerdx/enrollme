import { useState } from "react";
import { toast, ToastContainer } from "react-toastify";
import { TypeAnimation } from "react-type-animation";
import ParticleBackground from "../components/ParticleBackground";
import "react-toastify/dist/ReactToastify.css";

export default function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("student");
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(true);

  const toggleTheme = () => setDarkMode(!darkMode);

  const handleSubmit = (e) => {
    e.preventDefault();

    // Optionally validate role
    if (!role) {
      toast.error("Please select a role.");
      return;
    }

    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      toast.success(`Registered as ${role}!`);
      // Simulate redirect or API call here
    }, 1500);
  };

  const handleRoleChange = (e) => {
    setRole(e.target.value);
  };

  const darkBackground = "linear-gradient(135deg, #1e1e2f, #2c3e50)";
  const lightBackground = "linear-gradient(135deg, #f2f7fd, #dbeafe)";

  return (
    <div
      className="position-relative"
      style={{
        height: "100vh",
        width: "100vw",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: darkMode ? darkBackground : lightBackground,
        transition: "background 0.5s ease-in-out",
        overflow: "hidden",
      }}
    >
      <ParticleBackground />

      <button
        onClick={toggleTheme}
        className={`btn btn-sm ${
          darkMode ? "btn-outline-light" : "btn-outline-dark"
        } position-absolute top-0 end-0 m-3`}
      >
        {darkMode ? "🌙" : "☀️"}
      </button>

      <div
        className="shadow-lg p-4"
        style={{
          width: "100%",
          maxWidth: "460px",
          borderRadius: "20px",
          backdropFilter: "blur(20px)",
          backgroundColor: darkMode
            ? "rgba(255,255,255,0.08)"
            : "rgba(240, 248, 255, 0.85)",
          border: "1px solid rgba(255,255,255,0.2)",
          color: darkMode ? "#fff" : "#212529",
        }}
      >
        <div className="text-center mb-4">
          <img
            src="https://cdn-icons-png.flaticon.com/512/5087/5087579.png"
            alt="EnrollMe"
            width="60"
            className="mb-3"
            style={{ transition: "transform 0.3s ease", cursor: "pointer" }}
            onMouseEnter={(e) => (e.target.style.transform = "scale(1.1)")}
            onMouseLeave={(e) => (e.target.style.transform = "scale(1)")}
          />
          <h3 className="fw-bold">Create Your Account</h3>
          <TypeAnimation
            sequence={[
              "Join the learning revolution 📘",
              2000,
              "Get started with EnrollMe 🚀",
              2000,
            ]}
            wrapper="p"
            speed={50}
            className="small"
            style={{
              color: darkMode ? "#ffffffcc" : "#1e293b",
              fontWeight: "600",
              fontSize: "0.95rem",
              textShadow: !darkMode ? "0 0 1px rgba(0,0,0,0.05)" : "none",
            }}
          />
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group mb-3">
            <label>Full Name</label>
            <input
              type="text"
              className="form-control"
              placeholder="John Doe"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </div>

          <div className="form-group mb-3">
            <label>Email address</label>
            <input
              type="email"
              className="form-control"
              placeholder="you@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="form-group mb-3">
            <label>Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <div className="form-group mb-4">
            <label>Select Role</label>
            <select
              name="role"
              className="form-select"
              value={role}
              onChange={handleRoleChange}
              required
            >
              <option value="student">Student</option>
              <option value="mentor">Mentor</option>
              <option value="admin">Admin</option>
            </select>
          </div>

          <button
            type="submit"
            className="btn btn-outline-success w-100 py-2 fw-semibold"
            style={{ borderRadius: "50px" }}
            disabled={loading}
          >
            {loading ? "Registering..." : "Register"}
          </button>
        </form>

        <div className="text-center mt-4 small">
          Already have an account?{" "}
          <a href="/login" className="text-decoration-underline">
            Login here
          </a>
        </div>
      </div>

      <ToastContainer position="top-center" autoClose={2000} />
    </div>
  );
}
