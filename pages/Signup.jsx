import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './styles.css';

export default function Signup() {
  const [form, setForm] = useState({ name: '', email: '', password: '', confirm: '' });
  const navigate = useNavigate();

  const handleSignup = async () => {
    if (form.password !== form.confirm) return alert("Passwords don't match");
    try {
      await axios.post('http://localhost:5000/api/signup', {
        name: form.name,
        email: form.email,
        password: form.password,
      });
      window.location.href = 'http://localhost:8501';  // User dashboard
    } catch (err) {
      alert('Signup failed');
    }
  };

  return (
    <div className="container">
      <img src="SRA_Logo.jpg" className="logo" alt="Logo" />
      <div className="form-box">
        <h2>SIGNUP</h2>
        <input placeholder="Enter your name" onChange={(e) => setForm({ ...form, name: e.target.value })} />
        <input placeholder="Enter your email" onChange={(e) => setForm({ ...form, email: e.target.value })} />
        <input type="password" placeholder="Enter your password" onChange={(e) => setForm({ ...form, password: e.target.value })} />
        <input type="password" placeholder="Confirm your password" onChange={(e) => setForm({ ...form, confirm: e.target.value })} />
        <button className="sb" onClick={handleSignup}>SIGNUP</button>
        <p onClick={() => navigate('/login')} className="link">Already have account LOGIN</p>
      </div>
    </div>
  );
}
