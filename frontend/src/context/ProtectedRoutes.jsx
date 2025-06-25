import React, { useContext } from "react";
import { Navigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";

const ProtectedRoute = ({ allowedRoles, children }) => {
  const { currentUser, loading } = useContext(UserContext);

  if (loading) return <div className="p-5">Loading...</div>;

  if (!currentUser) return <Navigate to="/login" />;

  if (!allowedRoles.includes(currentUser.role)) return <Navigate to="/dashboard" />;

  return children;
};

export default ProtectedRoute;
