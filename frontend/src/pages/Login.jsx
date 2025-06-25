import { useState, useContext } from "react";
import { ToastContainer } from "react-toastify";
import { TypeAnimation } from "react-type-animation";
import ParticleBackground from "../components/ParticleBackground";
import "react-toastify/dist/ReactToastify.css";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(true);

  const { login_user } = useContext(UserContext);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const res = await login_user(email, password);
    setLoading(false);

    if (res) {
      navigate("/Dashboard"); 
    }
  };

  const toggleTheme = () => setDarkMode(!darkMode);

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
          maxWidth: "420px",
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
          <h3 className="fw-bold">Welcome Back</h3>
          <TypeAnimation
            sequence={[
              "Sign in to continue 🚀",
              2000,
              "Welcome to EnrollMe 👋",
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
            <label>Email address</label>
            <input
              type="email"
              className="form-control"
              placeholder="name@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="form-group mb-4">
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

          <button
            type="submit"
            className="btn btn-outline-primary w-100 py-2 fw-semibold"
            style={{ borderRadius: "50px" }}
            disabled={loading}
          >
            {loading ? "Logging in..." : "Log In"}
          </button>
        </form>

        <div className="text-center mt-4 small">
          No account?{" "}
          <a href="/register" className="text-decoration-underline">
            Register here
          </a>
        </div>
      </div>

      <ToastContainer position="top-center" autoClose={2000} />
    </div>
  );
}
