import React, { createContext, useState, useEffect } from "react";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";

export const UserContext = createContext();

const UserProviderWrapper = ({ children }) => {
  const navigate = useNavigate();

  const [user, setUser] = useState(null);
  const [authToken, setAuthToken] = useState(() => localStorage.getItem("access_token"));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (authToken) {
      fetch("http://localhost:5000/Users/me", {
        method: "GET",
        headers: { Authorization: `Bearer ${authToken}` },
      })
        .then(res => res.json())
        .then(data => {
          console.log("Fetched /Users/me:", data);
          if (data.error) {
            toast.error(data.error);
            setUser(null);
          } else {
            setUser(data);
          }
        })
        .catch(err => {
          toast.error("Failed to fetch user data.");
          console.error(err);
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, [authToken]);

  
const register_user = (username, email, password, role) => {
  toast.loading("Registering...");

  fetch("http://localhost:5000/Users", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, email, password, role }),
  })
    .then(res => res.json())
    .then(data => {
      toast.dismiss();

      if (data.error) {
        toast.error(data.error);
      } else {
        toast.success("Registration successful!");
        navigate("/login");
      }
    })
    .catch(err => {
      toast.dismiss();
      toast.error("Registration failed.");
      console.error(err);
    });
};

  const login_user = (email, password) => {
    toast.loading("Logging in...");
    return fetch("http://localhost:5000/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    })
      .then(res => res.json())
      .then(data => {
        toast.dismiss();
        if (data.error) {
          toast.error(data.error);
          return null;
        } else {
          localStorage.setItem("access_token", data.access_token);
          setAuthToken(data.access_token);
          setUser(data.user);
          toast.success("Login successful!");

          navigate("/dashboard");

          return data;
        }
      })
      .catch(err => {
        toast.dismiss();
        toast.error("Login failed.");
        console.error(err);
        return null;
      });
  };

  const logout_user = () => {
    fetch("http://localhost:5000/logout", {
      method: "DELETE",
      headers: { Authorization: `Bearer ${authToken}` },
    })
      .then(res => res.json())
      .then(data => {
        if (data.success) toast.success(data.success);
        else toast.info("Logged out.");

        localStorage.removeItem("access_token");
        setAuthToken(null);
        setUser(null);
        navigate("/login");
      })
      .catch(err => {
        toast.error("Logging out.");
        console.error(err);
      });
  };

  return (
    <UserContext.Provider
      value={{
        user,
        authToken,
        loading,
        register_user,
        login_user,
        logout_user,
      }}
    >
      {children}
    </UserContext.Provider>
  );
};

export default UserProviderWrapper;
