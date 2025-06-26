import React, { useState, useEffect, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { toast } from "react-toastify";

export default function AdminDashboard() {
  const { authToken } = useContext(UserContext);
  const [users, setUsers] = useState([]);
  const baseURL = import.meta.env.VITE_API_BASE_URL;

  useEffect(() => {
    fetch(`${baseURL}/Users`, {
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) setUsers(data);
        else setUsers([]);
      })
      .catch(() => {
        toast.error("Failed to load users");
        setUsers([]);
      });
  }, [authToken, baseURL]);

  const handleDelete = (userId) => {
    if (!window.confirm("Are you sure you want to delete this user?")) return;

    fetch(`${baseURL}/Users/${userId}`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) toast.error(data.error);
        else {
          toast.success("User deleted!");
          setUsers((prev) => prev.filter((u) => u.id !== userId));
        }
      })
      .catch(() => toast.error("Failed to delete user"));
  };

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
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {users.map((u) => (
              <tr key={u.id}>
                <td>{u.name}</td>
                <td>{u.email}</td>
                <td>
                  <span
                    className={`badge bg-${
                      u.role === "admin"
                        ? "dark"
                        : u.role === "mentor"
                        ? "primary"
                        : "secondary"
                    } text-capitalize`}
                  >
                    {u.role}
                  </span>
                </td>
                <td>
                  <button
                    className="btn btn-sm btn-danger"
                    onClick={() => handleDelete(u.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
