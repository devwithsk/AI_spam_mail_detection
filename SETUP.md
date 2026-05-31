# 🛡️ Spam Detection Website - Professional Full Stack Application

A professional spam detection application built with Flask backend and React frontend. Features AI-powered spam detection with confidence scores for emails and SMS messages.

## 🚀 Features

✅ **Real-time Spam Detection** - Analyze emails and SMS instantly
✅ **Confidence Scores** - Get probability scores for predictions (0-100%)
✅ **Beautiful UI** - Modern, responsive React interface
✅ **Professional API** - RESTful Flask backend with error handling
✅ **Batch Processing** - Analyze multiple messages at once
✅ **CORS Enabled** - Easy frontend-backend integration
✅ **Production Ready** - Comprehensive error handling and logging

## 📁 Project Structure

```
spam_mail_detection/
├── app.py                 # Flask backend API
├── main.py               # Model training script
├── requirements.txt      # Python dependencies
├── model.pkl            # Trained ML model (generated)
├── vectorizer.pkl       # TF-IDF vectorizer (generated)
├── mail_data.csv        # Training dataset
│
└── frontend/
    ├── package.json     # React dependencies
    ├── public/
    │   └── index.html   # HTML entry point
    └── src/
        ├── App.jsx      # Main React component
        ├── App.css      # Styles
        ├── index.jsx    # React entry point
        └── index.css    # Global styles
```

## 🔧 Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+ and npm
- Git (optional)

### Step 1: Train the Model

```bash
cd spam_mail_detection
python main.py
```

This will:
- Load the mail dataset
- Train the Naive Bayes model
- Generate `model.pkl` and `vectorizer.pkl`
- Display accuracy metrics

Expected output:
```
✓ Model and Vectorizer loaded successfully!
Accuracy: 0.97
```

### Step 2: Install Backend Dependencies

```bash
# Install Python packages
pip install -r requirements.txt
```

**Required packages:**
- flask==2.3.2 - Web framework
- flask-cors==4.0.0 - CORS support
- scikit-learn==1.2.2 - ML library
- joblib==1.2.0 - Model serialization
- pandas==2.0.0 - Data processing

### Step 3: Start Flask Backend

```bash
python app.py
```

Backend will run on: **http://localhost:5000**

✓ You'll see:
```
🚀 Spam Detection API Starting...
📍 Server: http://localhost:5000
📚 API Docs: http://localhost:5000
```

### Step 4: Install Frontend Dependencies

Open a new terminal in the `frontend` directory:

```bash
cd frontend
npm install
```

### Step 5: Start React Frontend

```bash
npm start
```

Frontend will run on: **http://localhost:3000**

## 🎯 API Documentation

### Endpoints

#### 1. **GET** `/`
Home endpoint - API status and available endpoints

**Response:**
```json
{
  "status": "success",
  "message": "Spam Detection API is running",
  "version": "1.0.0"
}
```

#### 2. **GET** `/api/health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2026-05-31T10:30:00"
}
```

#### 3. **POST** `/api/predict`
Analyze a single message

**Request:**
```json
{
  "message": "Congratulations! You won a free iPhone. Click here now."
}
```

**Response (SPAM):**
```json
{
  "status": "success",
  "prediction": "spam",
  "label": "🚨 SPAM",
  "confidence": 97.5,
  "message": "Congratulations! You won a free iPhone...",
  "timestamp": "2026-05-31T10:30:00"
}
```

**Response (HAM/SAFE):**
```json
{
  "status": "success",
  "prediction": "ham",
  "label": "✅ SAFE MESSAGE",
  "confidence": 98.2,
  "message": "Hi, how are you doing?",
  "timestamp": "2026-05-31T10:30:00"
}
```

#### 4. **POST** `/api/batch-predict`
Analyze multiple messages (max 100)

**Request:**
```json
{
  "messages": [
    "Free money! Click here",
    "Hi, how are you?",
    "You've won a prize!"
  ]
}
```

**Response:**
```json
{
  "status": "success",
  "count": 3,
  "results": [
    {
      "message": "Free money! Click here",
      "prediction": "spam",
      "label": "🚨 SPAM",
      "confidence": 95.3
    },
    {
      "message": "Hi, how are you?",
      "prediction": "ham",
      "label": "✅ SAFE MESSAGE",
      "confidence": 99.1
    },
    {
      "message": "You've won a prize!",
      "prediction": "spam",
      "label": "🚨 SPAM",
      "confidence": 94.2
    }
  ]
}
```

## 🧪 Testing the API

### Using cURL

```bash
# Single prediction
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"message":"Free iPhone! Click now"}'

# Batch prediction
curl -X POST http://localhost:5000/api/batch-predict \
  -H "Content-Type: application/json" \
  -d '{"messages":["Hello","Free money!"]}'
```

### Using Python

```python
import requests

API_URL = "http://localhost:5000"

# Single message
response = requests.post(
    f"{API_URL}/api/predict",
    json={"message": "Free iPhone! Click now"}
)
print(response.json())

# Batch messages
response = requests.post(
    f"{API_URL}/api/batch-predict",
    json={"messages": ["Hello", "Free money!"]}
)
print(response.json())
```

## 🎨 Frontend Features

### User Interface

1. **Text Input Area**
   - Drag & drop support (optional)
   - Character counter (0-10000)
   - Keyboard shortcut: Ctrl+Enter to submit

2. **Analysis Results**
   - Large visual indicator (SPAM/SAFE)
   - Animated confidence bar
   - Color-coded results (red for spam, green for safe)
   - Original message display
   - Timestamp

3. **Loading State**
   - Spinner animation
   - Disabled buttons during analysis
   - Real-time feedback

4. **Error Handling**
   - Validation error messages
   - Network error recovery
   - User-friendly error display

### Responsive Design

- ✅ Mobile-friendly (iOS, Android)
- ✅ Tablet optimized
- ✅ Desktop enhanced
- ✅ Dark mode compatible

## 📊 Model Information

### Architecture
- **Algorithm**: Multinomial Naive Bayes
- **Vectorizer**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Language**: English
- **Features**: Top 5000 words

### Performance
- **Accuracy**: ~97%
- **Training Data**: 5,572 messages
- **Output Classes**: 2 (spam, ham)

### How It Works

1. **Text Preprocessing**
   - Convert to lowercase
   - Remove English stopwords
   - Tokenize

2. **Vectorization**
   - Convert text to TF-IDF matrix
   - Use pre-trained vectorizer

3. **Classification**
   - Naive Bayes probability calculation
   - Return confidence score

## 🛠️ Advanced Usage

### Environment Variables

Create a `.env` file in the frontend directory:

```env
# Frontend (.env)
REACT_APP_API_URL=http://localhost:5000

# Backend (.env) - optional
FLASK_ENV=development
FLASK_DEBUG=True
```

### Customizing the Model

To train on new data:

```python
# In main.py, modify:
df = pd.read_csv("your_data.csv")  # Your dataset

# Adjust parameters:
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=5000,  # Increase/decrease features
    ngram_range=(1, 2)  # Use bigrams
)
```

### Production Deployment

#### Backend (Flask)

For production, use Gunicorn:

```bash
# Install
pip install gunicorn

# Run
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Frontend (React)

Build for production:

```bash
cd frontend
npm run build
```

This creates an optimized `build/` folder for deployment.

## 🔐 Security Features

✅ **CORS Protection** - Configurable origins
✅ **Input Validation** - Message length limits
✅ **Error Handling** - No sensitive data in responses
✅ **Rate Limiting** - (Optional, can be added)

## 📈 Performance

| Metric | Value |
|--------|-------|
| API Response Time | < 100ms |
| Frontend Load Time | < 2s |
| Model Accuracy | 97% |
| Max Batch Size | 100 messages |
| Max Message Length | 10,000 characters |

## 🐛 Troubleshooting

### Backend Issues

**Error: "Model not found"**
```bash
# Solution: Train the model first
python main.py
```

**Error: "Port 5000 already in use"**
```bash
# Solution: Use a different port
python -c "app.run(port=5001)"
```

**Error: "ModuleNotFoundError"**
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

### Frontend Issues

**Error: "Cannot GET /"**
- Make sure you ran `npm start` in the frontend directory
- Check that React is running on port 3000

**Error: "Failed to connect to server"**
- Make sure Flask backend is running on port 5000
- Check REACT_APP_API_URL environment variable

**Module not found errors**
```bash
# Solution: Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

## 📚 Documentation

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

## 🚀 Deployment

### Deploy to Heroku

**Backend:**
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
git push heroku main
```

**Frontend:**
```bash
# Build and deploy to Netlify
npm run build
# Upload build/ folder to Netlify
```

## 📝 License

This project is open source and available under the MIT License.

## 💡 Future Enhancements

- [ ] Multi-language support
- [ ] Custom model training interface
- [ ] API key authentication
- [ ] Database integration
- [ ] Admin dashboard
- [ ] Email/SMS notification features
- [ ] Docker containerization
- [ ] Real-time model updates

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on GitHub or contact the development team.

---

**Built with ❤️ using Flask + React + AI**

🚀 **Happy spam detecting!**
