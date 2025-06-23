// src/pages/Profile.jsx
import React, { useEffect, useState, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { toast } from "react-toastify";

export default function Profile() {
  const { auth_token } = useContext(UserContext);
  const [profile, setProfile] = useState(null);
  const [bio, setBio] = useState("");
  const [avatarUrl, setAvatarUrl] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5000/Profiles/me", {
      headers: { Authorization: `Bearer ${auth_token}` },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) toast.error(data.error);
        else {
          setProfile(data);
          setBio(data.bio || "");
          setAvatarUrl(data.avatar_url || "");
        }
      })
      .catch(() => toast.error("Failed to fetch profile"))
      .finally(() => setLoading(false));
  }, [auth_token]);

  const handleUpdate = () => {
    fetch("http://localhost:5000/Profiles/me", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${auth_token}`,
      },
      body: JSON.stringify({ bio, avatar_url: avatarUrl }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) toast.error(data.error);
        else toast.success("Profile updated successfully");
      })
      .catch(() => toast.error("Update failed"));
  };

  if (loading) return <div className="text-center mt-5 text-light">Loading...</div>;

  return (
    <div
      className="min-vh-100 py-5"
      style={{
        background: "radial-gradient(circle at top left, #0f172a, #1e293b)",
        color: "#f1f5f9",
      }}
    >
      <div className="container" style={{ maxWidth: "600px" }}>
        <div
          className="p-4 rounded-4 shadow-sm"
          style={{
            background: "rgba(255, 255, 255, 0.05)",
            backdropFilter: "blur(14px)",
            borderRadius: "1rem",
            border: "1px solid rgba(255,255,255,0.1)",
          }}
        >
          <h2
            className="fw-bold text-center mb-4"
            style={{
              background: "linear-gradient(90deg, #3b82f6, #ec4899)",
              WebkitBackgroundClip: "text",
              WebkitTextFillColor: "transparent",
            }}
          >
            🧑 My Profile
          </h2>

          <div className="mb-4 text-center">
            {avatarUrl ? (
              <img
                src={avatarUrl}
                alt="Avatar"
                className="rounded-circle border border-secondary"
                style={{ width: "120px", height: "120px", objectFit: "cover" }}
              />
            ) : (
              <div
                className="rounded-circle bg-secondary d-inline-block"
                style={{
                  width: "120px",
                  height: "120px",
                  lineHeight: "120px",
                  color: "#fff",
                  textAlign: "center",
                }}
              >
                No Avatar
              </div>
            )}
          </div>

          <div className="mb-3">
            <label className="form-label text-light">Bio</label>
            <textarea
              className="form-control bg-dark text-light border-secondary"
              value={bio}
              onChange={(e) => setBio(e.target.value)}
            />
          </div>

          <div className="mb-4">
            <label className="form-label text-light">Avatar URL</label>
            <input
              type="url"
              className="form-control bg-dark text-light border-secondary"
              value={avatarUrl}
              onChange={(e) => setAvatarUrl(e.target.value)}
              placeholder="https://example.com/avatar.png"
            />
          </div>
          

          

          <button className="btn btn-outline-light w-100" onClick={handleUpdate}>
            Update Profile
          </button>
        </div>
      </div>
    </div>
  );
}
