// src/pages/AdminDashboard.jsx
import React, { useState } from "react";

const dummyUsers = [
  { id: 1, name: "Fatuma Ali", email: "fatuma@example.com", role: "student" },
  { id: 2, name: "Alex Kariuki", email: "alex@example.com", role: "mentor" },
  { id: 3, name: "Mikerdx", email: "admin@example.com", role: "admin" },
];

export default function AdminDashboard() {
  const [users] = useState(dummyUsers);

  return (
    <div className="container py-4">
      <h3 className="fw-bold mb-4">🧑‍💼 Admin Dashboard</h3>

      <h5 className="mb-3">👥 All Users</h5>
      <div className="table-responsive">
        <table className="table table-hover align-middle">
          <thead className="table-light">
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Role</th>
            </tr>
          </thead>
          <tbody>
            {users.map((u) => (
              <tr key={u.id}>
                <td>{u.name}</td>
                <td>{u.email}</td>
                <td>
                  <span className={`badge bg-${
                    u.role === "admin"
                      ? "dark"
                      : u.role === "mentor"
                      ? "primary"
                      : "secondary"
                  } text-capitalize`}>
                    {u.role}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
