import React, { createContext, useState, useEffect } from 'react';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';

const UserContext = createContext(); // Declare first

const UserProvider = ({ children }) => {
  const navigate = useNavigate();
  const [currentUser, setCurrentUser] = useState(null);
  const [auth_token, setAuthToken] = useState(() => localStorage.getItem("access_token"));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (auth_token) {
      fetch(`http://localhost:5000/Users/me`, {
        method: "GET",
        headers: { "Authorization": `Bearer ${auth_token}` }
      })
        .then(res => res.json())
        .then(res => {
          if (res.error) toast.error(res.error);
          else setCurrentUser(res);
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, [auth_token]);

  function register_user(username, email, password) {
    toast.loading("Registering user...");
    fetch(`http://localhost:5000/Users`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password })
    })
      .then(res => res.json())
      .then(res => {
        toast.dismiss();
        res.error ? toast.error(res.error) :
          (toast.success(res.success), navigate("/login"));
      });
  }

  function login_user(email, password) {
    toast.loading("Logging in...");
    return fetch(`http://localhost:5000/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    })
      .then(res => res.json())
      .then(res => {
        toast.dismiss();
        if (res.error) {
          toast.error(res.error);
          return null;
        } else {
          localStorage.setItem("access_token", res.access_token);
          setAuthToken(res.access_token);
          toast.success("Logged in!");
          return res;
        }
      });
  }

  function logout_user() {
    fetch(`http://localhost:5000/logout`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${auth_token}` }
    })
      .then(res => res.json())
      .then(res => {
        toast.success(res.success);
        localStorage.removeItem("access_token");
        setAuthToken(null);
        setCurrentUser(null);
        navigate("/login");
      });
  }

  return (
    <UserContext.Provider value={{
      currentUser,
      auth_token,
      loading,
      register_user,
      login_user,
      logout_user
    }}>
      {children}
    </UserContext.Provider>
  );
};

// ✅ Export separately
export { UserContext, UserProvider };
