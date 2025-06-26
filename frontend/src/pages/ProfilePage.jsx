import React, { useEffect, useState, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { toast } from "react-toastify";

export default function Profile() {
  const { auth_token } = useContext(UserContext);
  const [profileExists, setProfileExists] = useState(false);
  const [bio, setBio] = useState("");
  const [avatarUrl, setAvatarUrl] = useState("");
  const [loading, setLoading] = useState(true);
  const [processing, setProcessing] = useState(false);
  const baseURL = import.meta.env.VITE_API_BASE_URL;

  const fetchProfile = () => {
    setLoading(true);
    fetch(`${baseURL}/Profiles/me`, {
      headers: { Authorization: `Bearer ${auth_token}` },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) {
          setProfileExists(false);
          setBio("");
          setAvatarUrl("");
        } else {
          setProfileExists(true);
          setBio(data.bio || "");
          setAvatarUrl(data.avatar_url || "");
        }
      })
      .catch(() => toast.error("Failed to fetch profile"))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    fetchProfile();
  }, [auth_token]);

  const handleCreate = () => {
    setProcessing(true);
    fetch(`${baseURL}/Profiles`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${auth_token}`,
      },
      body: JSON.stringify({ bio, avatar_url: avatarUrl }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) toast.error(data.error);
        else {
          toast.success("Profile created successfully");
          fetchProfile();
        }
      })
      .catch(() => toast.error("Create failed"))
      .finally(() => setProcessing(false));
  };

  const handleUpdate = () => {
    setProcessing(true);
    fetch(`${baseURL}/Profiles/me`, {
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
        else {
          toast.success("Profile updated successfully");
          fetchProfile();
        }
      })
      .catch(() => toast.error("Update failed"))
      .finally(() => setProcessing(false));
  };

  const handleDelete = () => {
    if (!window.confirm("Are you sure you want to delete your profile?")) return;
    setProcessing(true);
    fetch(`${baseURL}/Profiles/me`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${auth_token}` },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) toast.error(data.error);
        else {
          toast.success("Profile deleted successfully");
          setBio("");
          setAvatarUrl("");
          setProfileExists(false);
        }
      })
      .catch(() => toast.error("Delete failed"))
      .finally(() => setProcessing(false));
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

          {profileExists && (
            <div className="mb-4 text-center">
              <div className="mb-2">
                <strong>Bio:</strong>
                <div className="text-light">{bio || <span className="text-muted">No bio set.</span>}</div>
              </div>
              <div className="mb-2">
                <strong>Avatar:</strong>
                <div>
                  {avatarUrl ? (
                    <img
                      src={avatarUrl}
                      alt="Avatar"
                      className="rounded-circle border border-secondary"
                      style={{ width: "120px", height: "120px", objectFit: "cover" }}
                    />
                  ) : (
                    <span className="text-muted">No Avatar</span>
                  )}
                </div>
              </div>
            </div>
          )}

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
          <div className="d-flex gap-2">
            {!profileExists ? (
              <button
                className="btn btn-success flex-grow-1"
                onClick={handleCreate}
                disabled={processing}
              >
                {processing ? "Creating..." : "Create Profile"}
              </button>
            ) : (
              <>
                <button
                  className="btn btn-outline-light flex-grow-1"
                  onClick={handleUpdate}
                  disabled={processing}
                >
                  {processing ? "Updating..." : "Update Profile"}
                </button>
                <button
                  className="btn btn-danger flex-grow-1"
                  onClick={handleDelete}
                  disabled={processing}
                >
                  {processing ? "Deleting..." : "Delete Profile"}
                </button>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
