import React from 'react';

function StreamlitEmbed() {
  return (
    <div>
      <h1>Smart Resume Analyzer</h1>
      <iframe 
        title="Streamlit Resume Analyzer"
        width="100%" 
        height="800" 
        src="http://localhost:8501" // Streamlit app URL
        frameBorder="0"
      />
    </div>
  );
}

export default StreamlitEmbed;
