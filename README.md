# 🛡️ AI Spam Detection Website

A professional AI-powered spam detection application with Flask backend and React frontend.

## ⚡ Quick Start

### Windows
```bash
setup-windows.bat
```

### Linux/Mac
```bash
chmod +x setup-unix.sh
./setup-unix.sh
```

## 📖 Manual Setup
Frontend will run on: **http://localhost:3000**

## 🎯 Usage

1. Open http://localhost:3000 in your browser
2. Paste an email or SMS message
3. Click "⚡ Analyze"
4. Get instant results with confidence score

## 📊 Features

✅ Real-time spam detection
✅ Confidence scores (0-100%)
✅ Beautiful responsive UI
✅ Professional Flask API
✅ Batch processing support
✅ Error handling

## 📚 Full Documentation

See [SETUP.md](SETUP.md) for complete setup guide, API documentation, and advanced usage.

## 🏗️ Project Structure

```
spam_mail_detection/
├── app.py                 # Flask backend API
├── main.py               # Model training
├── requirements.txt      # Python deps
├── SETUP.md             # Complete guide
│
└── frontend/
    ├── package.json
    └── src/
        ├── App.jsx      # Main component
        └── App.css      # Styles
```

## 🔧 Tech Stack

**Backend:**
- Flask 2.3
- Scikit-learn (ML)
- Pandas (Data)

**Frontend:**
- React 18
- CSS3 (Modern animations)
- Responsive design

**ML Model:**
- Algorithm: Naive Bayes
- Vectorizer: TF-IDF
- Accuracy: ~97%

## ⚠️ Troubleshooting

### Model not found
```bash
python main.py  # Train first
```

### Port already in use
```bash
# Change port in app.py or frontend/.env
```

### Module errors
```bash
pip install -r requirements.txt
cd frontend && npm install
```

## 🚀 Deployment

- **Backend**: Heroku, AWS, DigitalOcean
- **Frontend**: Netlify, Vercel, GitHub Pages

## 📧 Support

For issues, check [SETUP.md](SETUP.md) troubleshooting section.

---

**Built with ❤️ - Flask + React + AI**
