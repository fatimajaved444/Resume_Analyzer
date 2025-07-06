import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './styles.css';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      await axios.post('http://localhost:5000/api/login', { email, password });
      window.location.href = 'http://localhost:8501';  // User dashboard
    } catch (err) {
      alert('Login failed');
    }
  };

  const handleAdminRedirect = () => {
    window.open('http://localhost:8502', '_blank'); // Assumes Streamlit Admin Dashboard runs on 8502
  };

  return (
    <div className="container">
      <img src="SRA_Logo.jpg" className="logo" alt="Logo" />
      <div className="form-box">
        <h2>LOGIN</h2>
        <input
          placeholder="Enter your email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Enter your password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className='sb' onClick={handleLogin}>LOGIN</button>
        <p onClick={() => navigate('/signup')} className="link">
          create new account SIGNUP
        </p>
        <button className="admin-btn" onClick={handleAdminRedirect}>
          Admin Dashboard
        </button>
      </div>
    </div>
  );
}
