import React, { useContext } from "react";
import { UserContext } from "../../context/UserContext";

const Dashboard = () => {
  const { currentUser } = useContext(UserContext);

  if (!currentUser) {
    return (
      <div className="min-vh-100 vw-100 d-flex justify-content-center align-items-center text-center bg-light">
        <p className="text-muted">Loading your dashboard...</p>
      </div>
    );
  }

  return (
    <div className="min-vh-100 vw-100 d-flex flex-column justify-content-center align-items-center text-center bg-light px-3">
      <h1 className="mb-3 text-primary fw-bold">
        Welcome, {currentUser.username}
      </h1>
      <p className="lead text-dark">Your Role: <strong>{currentUser.role}</strong></p>
    </div>
  );
};

export default Dashboard;