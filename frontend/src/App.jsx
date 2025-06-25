import { Routes, Route, useLocation } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Courses from "./pages/Courses";
import StudentDashboard from "./pages/StudentDashboard";
import AdminDashboard from "./pages/AdminDashboard";
import MentorDashboard from "./pages/MentorDashboard";
import ProfilePage from "./pages/ProfilePage";
import Sidebar from "./components/Sidebar";
import { useContext } from "react";
import { UserContext } from "./context/UserContext";

function App() {
  const { user } = useContext(UserContext);
  const location = useLocation();

  const showSidebar =
    user &&
    !["/login", "/register", "/"].includes(location.pathname);


  return (
    <div className="d-flex flex-column min-vh-100 w-100">
      <div className="flex-grow-1 w-100 d-flex">
        {showSidebar && (
          <Sidebar role={user?.role} darkMode={true} />
        )}
        <div className="flex-grow-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/dashboard" element={<Dashboard />}>
              <Route index element={<StudentDashboard />} />
              <Route path="admin" element={<AdminDashboard />} />
              <Route path="mentor" element={<MentorDashboard />} />
              <Route path="courses" element={<Courses />} />
            </Route>
            <Route path="/courses" element={<Courses />} />
            <Route path="/profile" element={<ProfilePage />} />
          </Routes>
        </div>
      </div>
    </div>
  );
}

export default App;