import React, { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

  const handleAnalyze = async () => {
    // Validation
    if (!message.trim()) {
      setError("Please enter an email or SMS message");
      return;
    }

    if (message.length > 10000) {
      setError("Message is too long (max 10000 characters)");
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/api/predict`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: message.trim() }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || "Prediction failed");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(
        err.message || "Failed to analyze message. Is the server running?"
      );
      console.error("Error:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setMessage("");
    setResult(null);
    setError(null);
  };

  const handleKeyPress = (e) => {
    if (e.ctrlKey && e.key === "Enter") {
      handleAnalyze();
    }
  };

  return (
    <div className="app">
      <div className="container">
        {/* Header */}
        <header className="header">
          <div className="header-content">
            <h1 className="title">
              🛡️ Spam Detection
            </h1>
            <p className="subtitle">
              AI-powered spam detection for emails and SMS
            </p>
          </div>
        </header>

        {/* Main Content */}
        <main className="main-content">
          {/* Input Section */}
          <div className="input-section">
            <label htmlFor="message-input" className="label">
              📧 Paste your Email or SMS
            </label>
            <textarea
              id="message-input"
              className="textarea"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Enter your email or SMS text here..."
              rows="6"
              disabled={loading}
            />
            <p className="char-count">
              {message.length} / 10000 characters
            </p>

            {/* Button Group */}
            <div className="button-group">
              <button
                className={`btn btn-primary ${loading ? "loading" : ""}`}
                onClick={handleAnalyze}
                disabled={loading || !message.trim()}
              >
                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Analyzing...
                  </>
                ) : (
                  <>
                    ⚡ Analyze
                  </>
                )}
              </button>
              <button
                className="btn btn-secondary"
                onClick={handleClear}
                disabled={loading}
              >
                🔄 Clear
              </button>
            </div>
          </div>

          {/* Error Message */}
          {error && (
            <div className="error-box">
              <span className="error-icon">❌</span>
              <div>
                <p className="error-title">Error</p>
                <p className="error-message">{error}</p>
              </div>
            </div>
          )}

          {/* Result Section - Improved Design */}
          {result && (
            <div className={`result-section ${result.prediction}`}>
              <div className="result-wrapper">
                {/* Result Header with Label */}
                <div className={`result-header ${result.prediction}`}>
                  <span className="result-emoji">
                    {result.prediction === "spam" ? "🚨" : "✅"}
                  </span>
                  <span className="result-status">
                    {result.prediction === "spam" ? "SPAM DETECTED" : "SAFE MESSAGE"}
                  </span>
                </div>

                {/* Confidence Section */}
                <div className="result-body">
                  <div className="confidence-container">
                    <p className="confidence-label">
                      {result.prediction === "spam"
                        ? "Spam Probability"
                        : "Safety Probability"}
                    </p>
                    <div className="confidence-bar-container">
                      <div
                        className={`confidence-bar ${result.prediction}`}
                        style={{ width: `${result.confidence}%` }}
                      >
                        <span className="confidence-text">
                          {result.confidence}%
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* Detection Method Badge */}
                  {result.detection_method && (
                    <div className="detection-method">
                      <span className={`method-badge ${result.detection_method}`}>
                        {result.detection_method === "rule_based"
                          ? "🔐 Rule-Based Detection"
                          : "🤖 AI Detection"}
                      </span>
                    </div>
                  )}

                  {/* Reason if available */}
                  {result.reason && (
                    <div className="reason-box">
                      <p className="reason-label">Detection Reason:</p>
                      <p className="reason-text">{result.reason}</p>
                    </div>
                  )}

                  {/* Message Content */}
                  <div className="message-section">
                    <p className="section-label">📝 Your Message:</p>
                    <div className="message-content">
                      {result.message}
                    </div>
                  </div>

                  {/* Timestamp */}
                  <p className="timestamp">
                    🕒 {new Date(result.timestamp).toLocaleString()}
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Info Box */}
          {!result && !loading && (
            <div className="info-box">
              <h3>ℹ️ How it works</h3>
              <ul>
                <li>
                  ✅ Paste your email or SMS text in the box above
                </li>
                <li>
                  🤖 Our AI analyzes it using advanced ML + phishing detection
                </li>
                <li>
                  🔍 Detects both common spam & phishing attempts
                </li>
                <li>
                  📊 Get instant results with confidence score
                </li>
                <li>
                  🔒 Your data is processed locally and not stored
                </li>
              </ul>
            </div>
          )}
        </main>

        {/* Footer */}
        <footer className="footer">
          <p>
            🚀 Spam Detection v1.0 | AI + Rule-Based Protection
          </p>
        </footer>
      </div>
    </div>
  );
}

export default App;
