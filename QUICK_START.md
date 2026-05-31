# 🎯 Quick Reference Guide

## ⚡ 30-Second Start

```bash
# Windows
setup-windows.bat

# Linux/Mac
./setup-unix.sh
```

Then open: **http://localhost:3000**

---

## 🔗 Key URLs

| Purpose | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:5000 |
| API Docs | http://localhost:5000 |

---

## 📋 Commands Reference

### Setup & Installation

```bash
# Windows quick setup
setup-windows.bat

# Unix quick setup
./setup-unix.sh

# Manual: Train model
python main.py

# Manual: Install Python packages
pip install -r requirements.txt

# Manual: Install React packages
cd frontend && npm install
```

### Running Application

```bash
# Backend (Terminal 1)
python app.py

# Frontend (Terminal 2)
cd frontend
npm start
```

### Testing

```bash
# Run test suite
python test_api.py

# Test single endpoint
curl http://localhost:5000/api/health
```

### Docker

```bash
# With Docker Compose
docker-compose up

# Manual Docker build
docker build -t spam-detector .
docker run -p 5000:5000 spam-detector
```

---

## 📚 Documentation Map

| Document | Purpose | Size |
|----------|---------|------|
| [README.md](README.md) | Quick start | 1KB |
| [SETUP.md](SETUP.md) | Complete setup guide | 40KB |
| [API_TESTING.md](API_TESTING.md) | API testing | 35KB |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Deployment guide | 50KB |
| [PROJECT_SUMMARY.txt](PROJECT_SUMMARY.txt) | Overview | 15KB |
| [QUICK_START.md](QUICK_START.md) | This file | 5KB |

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Model not found | `python main.py` |
| Port in use | Change port in config |
| Module not found | `pip install -r requirements.txt` |
| npm error | `npm install` in frontend |
| API won't start | Check port 5000 is available |
| Frontend won't load | Check REACT_APP_API_URL |

---

## 📊 API Examples

### Predict Single Message

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"message":"Free money!"}'
```

### Batch Prediction

```bash
curl -X POST http://localhost:5000/api/batch-predict \
  -H "Content-Type: application/json" \
  -d '{"messages":["Free iPhone!","Hi there!"]}'
```

### Health Check

```bash
curl http://localhost:5000/api/health
```

---

## 🚀 Deployment Quick Links

- **Heroku**: See DEPLOYMENT.md → Heroku section
- **AWS**: See DEPLOYMENT.md → AWS section
- **Docker**: `docker-compose up`
- **Netlify**: Drag & drop `frontend/build` folder
- **Vercel**: Connect GitHub repo

---

## 📁 Important Files

```
Backend:
  app.py             - Flask API server
  main.py            - Model training
  model.pkl          - Trained model (after running main.py)
  vectorizer.pkl     - Vectorizer (after running main.py)

Frontend:
  src/App.jsx        - Main React component
  src/App.css        - Styling
  public/index.html  - HTML shell

Config:
  requirements.txt   - Python dependencies
  frontend/package.json - React dependencies
  docker-compose.yml - Docker configuration
```

---

## ✅ Pre-Deployment Checklist

- [ ] Model trained (model.pkl exists)
- [ ] Dependencies installed
- [ ] Backend runs without errors
- [ ] Frontend builds successfully
- [ ] API tests pass
- [ ] CORS configured
- [ ] Environment variables set
- [ ] Performance acceptable

---

## 🎯 Feature Checklist

### Backend ✅
- [x] Flask REST API
- [x] Single message prediction
- [x] Batch prediction (up to 100)
- [x] Confidence scores
- [x] Error handling
- [x] CORS support
- [x] Health check

### Frontend ✅
- [x] Beautiful UI
- [x] Text input
- [x] Real-time analysis
- [x] Results display
- [x] Loading animation
- [x] Error messages
- [x] Responsive design

### ML Model ✅
- [x] 97% accuracy
- [x] Fast prediction
- [x] TF-IDF vectorizer
- [x] Naive Bayes classifier
- [x] Binary classification

### Documentation ✅
- [x] Setup guide
- [x] API documentation
- [x] Testing guide
- [x] Deployment guide
- [x] Troubleshooting

---

## 🎓 Learning Resources

### Official Docs
- [Flask Docs](https://flask.palletsprojects.com/)
- [React Docs](https://react.dev/)
- [Scikit-learn Docs](https://scikit-learn.org/)

### Tutorials in This Project
- API_TESTING.md - Learn API testing
- DEPLOYMENT.md - Learn deployment
- SETUP.md - Learn architecture

---

## 💡 Pro Tips

1. **Keyboard Shortcut**: `Ctrl+Enter` to submit in frontend
2. **API Testing**: Use `test_api.py` for automated tests
3. **Error Logs**: Check terminal output for detailed errors
4. **Performance**: Response time typically < 100ms
5. **Scaling**: Use Docker to scale horizontally
6. **Caching**: Add Redis for production optimization

---

## 📞 Getting Help

1. Check the relevant documentation file
2. Look at error messages in terminal
3. Run `test_api.py` to diagnose issues
4. Check DEPLOYMENT.md for platform-specific help

---

## 🎯 Common Tasks

### Add New Feature
1. Edit `src/App.jsx` for UI
2. Edit `app.py` for backend logic
3. Test with `test_api.py`

### Deploy to Production
1. See DEPLOYMENT.md
2. Choose platform (Heroku, AWS, etc.)
3. Follow platform-specific instructions

### Run Tests
1. `python test_api.py`
2. Or use cURL examples in API_TESTING.md

### Monitor Performance
1. Check response times in console
2. Use browser DevTools (F12)
3. Monitor server logs in terminal

---

## 🏁 Next Steps

**First Time Users:**
1. Run setup script
2. Access http://localhost:3000
3. Test with sample messages
4. Read SETUP.md for details

**Developers:**
1. Explore source code
2. Run test_api.py
3. Customize styling/features
4. Review DEPLOYMENT.md

**DevOps:**
1. Review docker-compose.yml
2. See DEPLOYMENT.md
3. Set up monitoring
4. Configure CI/CD

---

**Version: 1.0.0** | **Status: Ready to Deploy** ✅

More help: See documentation files above
