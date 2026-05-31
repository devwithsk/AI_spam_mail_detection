"""
Spam Detection Flask Backend API
Professional API for spam detection service
"""

import os
import json
import joblib
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

# =========================
# FLASK APP SETUP
# =========================

app = Flask(__name__)
CORS(app)

# =========================
# LOAD TRAINED MODEL
# =========================

MODEL_PATH = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("✓ Model and Vectorizer loaded successfully!")
except FileNotFoundError as e:
    print(f"✗ Error: {e}")
    print("Please run: python main.py (to train the model first)")
    model = None
    vectorizer = None

# =========================
# API ROUTES
# =========================

@app.route("/", methods=["GET"])
def home():
    """Home endpoint - API status check"""
    return jsonify({
        "status": "success",
        "message": "Spam Detection API is running",
        "version": "1.0.0",
        "endpoints": {
            "POST /api/predict": "Predict if message is spam",
            "GET /api/health": "Health check",
            "GET /": "API info"
        }
    }), 200


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    model_loaded = model is not None and vectorizer is not None
    return jsonify({
        "status": "healthy",
        "model_loaded": model_loaded,
        "timestamp": datetime.now().isoformat()
    }), 200


def check_phishing_keywords(text):
    """Check if message contains phishing keywords"""
    phishing_keywords = [
        "urgent",
        "unauthorized",
        "login",
        "verify your account",
        "account locked",
        "click the link",
        "click here",
        "within 24 hours",
        "confirm your",
        "permanent suspension",
        "suspended",
        "security team",
        "verify now",
        "update your",
        "confirm identity",
        "unusual activity",
        "suspicious activity",
        "restricted",
        "action required",
        "re-confirm",
        "re-enter",
        "valid your",
        "validate your",
        "congratulations won",
        "claim your",
        "free money",
        "prize",
        "inheritance",
        "refund",
        "tax refund",
        "dear customer",
        "dear user",
        "dear friend",
        "act now",
        "limited time",
        "hurry",
        "expire",
        "expiring"
    ]
    
    text_lower = text.lower()
    keyword_count = sum(1 for keyword in phishing_keywords if keyword in text_lower)
    
    return keyword_count >= 2, keyword_count


@app.route("/api/predict", methods=["POST"])
def predict():
    """
    Predict if a message is spam or not with enhanced detection
    """
    try:
        # Validate request
        if not request.json:
            return jsonify({"status": "error", "message": "Request body must be JSON"}), 400

        message = request.json.get("message", "").strip()

        if not message:
            return jsonify({"status": "error", "message": "Message cannot be empty"}), 400

        if len(message) > 10000:
            return jsonify({"status": "error", "message": "Message too long (max 10000 characters)"}), 400

        if model is None or vectorizer is None:
            return jsonify({"status": "error", "message": "Model not loaded. Please train the model first."}), 500

        # Rule-based phishing detection first
        has_phishing_keywords, keyword_count = check_phishing_keywords(message)
        if has_phishing_keywords:
            return jsonify({
                "status": "success",
                "prediction": "spam",
                "label": "🚨 SPAM (Phishing Detected)",
                "confidence": 99.0,
                "detection_method": "rule_based",
                "reason": f"Detected {keyword_count} phishing keywords",
                "message": message,
                "timestamp": datetime.now().isoformat()
            }), 200

        # ML-based detection
        message_vector = vectorizer.transform([message])
        probabilities = model.predict_proba(message_vector)[0]
        classes = model.classes_
        spam_idx = list(classes).index("spam") if "spam" in classes else 0
        spam_probability = float(probabilities[spam_idx])

        # Aggressive threshold for spam
        is_spam_by_ml = spam_probability >= 0.35
        confidence = round(spam_probability * 100, 2)
        result_label = "🚨 SPAM" if is_spam_by_ml else "✅ SAFE MESSAGE"

        return jsonify({
            "status": "success",
            "prediction": "spam" if is_spam_by_ml else "ham",
            "label": result_label,
            "confidence": confidence if is_spam_by_ml else round((1 - spam_probability) * 100, 2),
            "detection_method": "ml",
            "message": message,
            "timestamp": datetime.now().isoformat()
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": f"Prediction error: {str(e)}"}), 500


@app.route("/api/batch-predict", methods=["POST"])
def batch_predict():
    """
    Predict multiple messages at once
    
    Request body:
    {
        "messages": ["message1", "message2", ...]
    }
    """
    
    try:
        if not request.json:
            return jsonify({
                "status": "error",
                "message": "Request body must be JSON"
            }), 400
        
        messages = request.json.get("messages", [])
        
        if not isinstance(messages, list):
            return jsonify({
                "status": "error",
                "message": "Messages must be a list"
            }), 400
        
        if len(messages) == 0:
            return jsonify({
                "status": "error",
                "message": "Messages list cannot be empty"
            }), 400
        
        if len(messages) > 100:
            return jsonify({
                "status": "error",
                "message": "Maximum 100 messages per request"
            }), 400
        
        if model is None or vectorizer is None:
            return jsonify({
                "status": "error",
                "message": "Model not loaded"
            }), 500
        
        # Vectorize all messages
        messages_vector = vectorizer.transform(messages)
        
        # Make predictions
        predictions = model.predict(messages_vector)
        probabilities = model.predict_proba(messages_vector)
        
        # Format results
        results = []
        for i, (msg, pred, probs) in enumerate(zip(messages, predictions, probabilities)):
            confidence = float(np.max(probs))
            is_spam = pred == "spam"
            results.append({
                "message": msg,
                "prediction": "spam" if is_spam else "ham",
                "label": "🚨 SPAM" if is_spam else "✅ SAFE MESSAGE",
                "confidence": round(confidence * 100, 2)
            })
        
        return jsonify({
            "status": "success",
            "count": len(results),
            "results": results,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Batch prediction error: {str(e)}"
        }), 500


# =========================
# ERROR HANDLERS
# =========================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 Spam Detection API Starting...")
    print("="*50)
    print("📍 Server: http://localhost:5000")
    print("📚 API Docs: http://localhost:5000")
    print("="*50 + "\n")
    
    app.run(debug=True, host="0.0.0.0", port=5000)
