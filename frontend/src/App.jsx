import { Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/shared/Home";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import Dashboard from "./pages/shared/Dashboard";
import Profile from "./pages/shared/Profile";
import NotFound from "./pages/shared/NotFound";
import Reviews from "./pages/shared/Reviews";
import AdminDashboard from "./pages/admin/AdminDashboard";
import ManageCourses from "./pages/admin/ManageCourses";
import AddCourse from "./pages/admin/AddCourse";
import ManageUsers from "./pages/admin/ManageUsers";
import ManageEnrollments from "./pages/admin/ManageEnrollments";
import MentorCourses from "./pages/mentor/MentorCourses";
import EditCourse from "./pages/mentor/EditCourse";
import BrowseCourses from "./pages/student/BrowseCourses";
import MyEnrollments from "./pages/student/MyEnrollments";
import AddReview from "./pages/student/AddReview";
import MyReviews from "./pages/student/MyReviews";

function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/reviews" element={<Reviews />} />

        {/* Admin */}
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
        <Route path="/admin/courses" element={<ManageCourses />} />
        <Route path="/admin/add-course" element={<AddCourse />} />
        <Route path="/admin/users" element={<ManageUsers />} />
        <Route path="/admin/enrollments" element={<ManageEnrollments />} />

        {/* Mentor */}
        <Route path="/mentor/courses" element={<MentorCourses />} />
        <Route path="/mentor/edit-course/:id" element={<EditCourse />} />

        {/* Student */}
        <Route path="/courses" element={<BrowseCourses />} />
        <Route path="/my-enrollments" element={<MyEnrollments />} />
        <Route path="/add-review/:courseId" element={<AddReview />} />
        <Route path="/my-reviews" element={<MyReviews />} />

        {/* Fallback */}
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}

export default App;
