import React from 'react';
import { useNavigate } from 'react-router-dom';
import './styles.css';

export default function Landing() {
  const navigate = useNavigate();
  return (
    <div className="container">
      <img src="SRA_Logo.jpg" className="logo" alt="Logo" />
      <div className="landing">
        <div className="left">
          <img src="l1.png" alt="Dream Job" className="poster" />
        </div>
        <div className="right">
          <h1>RESUSCAN</h1>
          <p  className='lpq'>
            Don't let your resume hold you back! Sign in today and take the first step toward your next big opportunity.
          </p>
          <button onClick={() => navigate('/signup')}>SIGNUP</button>
          <p onClick={() => navigate('/login')} className="link">Already have account LOGIN</p>
        </div>
      </div>
    </div>
  );
}
