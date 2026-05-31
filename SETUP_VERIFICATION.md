# 🎯 Configuration & Pre-Flight Checklist

## ✅ Pre-Setup Checklist

Before you start, make sure you have:

- [ ] Python 3.8+ installed (`python --version`)
- [ ] Node.js 14+ installed (`node --version`)
- [ ] npm installed (`npm --version`)
- [ ] Git installed (optional, `git --version`)
- [ ] 2GB free disk space
- [ ] Ports 5000 & 3000 available

---

## ✅ Installation Verification

### Step 1: Check Python

```bash
python --version
```
Expected: Python 3.8.0 or higher

```bash
pip --version
```
Expected: pip 20.0 or higher

### Step 2: Check Node.js

```bash
node --version
```
Expected: v14.0.0 or higher

```bash
npm --version
```
Expected: 6.0.0 or higher

### Step 3: Verify Project Structure

```bash
# Check main files exist
ls -la *.py
ls -la *.txt
ls -la frontend/
```

Expected files:
- ✓ app.py
- ✓ main.py
- ✓ requirements.txt
- ✓ frontend/package.json
- ✓ frontend/src/App.jsx

---

## ✅ Step-by-Step Setup Verification

### Phase 1: Model Training

```bash
# Step 1.1: Check dataset
ls -la mail_data.csv
```
Should show: mail_data.csv file exists

```bash
# Step 1.2: Train model
python main.py
```

Expected output:
```
Dataset Loaded Successfully!
Model Training Completed!
Accuracy: 0.97
Classification Report:
[...]
Model and Vectorizer Saved Successfully!
```

After this step, verify:
- [ ] model.pkl created
- [ ] vectorizer.pkl created
- [ ] No error messages
- [ ] Accuracy > 0.90

### Phase 2: Backend Setup

```bash
# Step 2.1: Check requirements
cat requirements.txt
```

Should show:
```
pandas==2.0.0
scikit-learn==1.2.2
joblib==1.2.0
flask==2.3.2
flask-cors==4.0.0
numpy==1.24.3
```

```bash
# Step 2.2: Install dependencies
pip install -r requirements.txt
```

Expected: All packages install successfully

```bash
# Step 2.3: Start backend (Terminal 1)
python app.py
```

Expected output:
```
🚀 Spam Detection API Starting...
📍 Server: http://localhost:5000
```

Verify:
- [ ] No error messages
- [ ] Server running on port 5000
- [ ] Ready for requests

### Phase 3: Frontend Setup

```bash
# Step 3.1: Navigate to frontend
cd frontend
```

```bash
# Step 3.2: Check package.json
cat package.json
```

Should contain React dependencies

```bash
# Step 3.3: Install dependencies
npm install
```

Expected: All packages install (may take 2-3 minutes)

```bash
# Step 3.4: Start frontend (Terminal 2)
npm start
```

Expected output:
```
Compiled successfully!
You can now view spam-detection-frontend in the browser.
Local: http://localhost:3000
```

Verify:
- [ ] Frontend loads in browser
- [ ] No blank page
- [ ] UI visible with input area

---

## ✅ Functionality Verification

### Test 1: API Health Check

```bash
curl http://localhost:5000/api/health
```

Expected response:
```json
{"status": "healthy", "model_loaded": true}
```

Verify: ✓ Status is "healthy"

### Test 2: Single Prediction

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"message":"Free iPhone!"}'
```

Expected response:
```json
{
  "status": "success",
  "prediction": "spam",
  "label": "🚨 SPAM",
  "confidence": 95.3
}
```

Verify:
- ✓ status is "success"
- ✓ prediction is "spam"
- ✓ confidence is a number
- ✓ Response time < 100ms

### Test 3: Frontend Submission

1. Open http://localhost:3000
2. Paste: "Congratulations! You won a free iPhone!"
3. Click "⚡ Analyze"
4. Wait for result

Verify:
- [ ] Result appears
- [ ] Shows "🚨 SPAM"
- [ ] Shows confidence %
- [ ] No error messages

### Test 4: Safe Message

1. In frontend, paste: "Hi, how are you doing?"
2. Click "⚡ Analyze"

Verify:
- [ ] Shows "✅ SAFE MESSAGE"
- [ ] Confidence > 90%
- [ ] Result displays correctly

### Test 5: Run Test Suite

```bash
python test_api.py
```

Expected: All tests should pass

Verify:
- [ ] "All tests passed" message
- [ ] No red X marks
- [ ] All endpoints tested

---

## ✅ Configuration Files

### Check Backend Config

File: `app.py`

Verify these lines exist:
```python
app = Flask(__name__)
CORS(app)
model = joblib.load(MODEL_PATH)
```

✓ Flask app created
✓ CORS enabled
✓ Model loaded

### Check Frontend Config

File: `frontend/src/App.jsx`

Verify:
```javascript
const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";
```

✓ API URL configured
✓ Default to localhost:5000

File: `frontend/public/index.html`

Verify:
```html
<div id="root"></div>
```

✓ Root element exists

---

## ✅ Environment Variables

### Frontend Environment

File: `frontend/.env` (or .env.local)

Optional - if needed:
```env
REACT_APP_API_URL=http://localhost:5000
```

### Backend Environment

Python variables in `app.py`:
```python
MODEL_PATH = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"
```

✓ Both files exist after training

---

## ✅ Port Availability

### Check if ports are in use

**Windows:**
```bash
netstat -ano | findstr :5000
netstat -ano | findstr :3000
```

Should return: Nothing (ports are free)

**Linux/Mac:**
```bash
lsof -i :5000
lsof -i :3000
```

Should return: Nothing (ports are free)

### If ports are in use

**Change Backend Port:**
Edit `app.py`:
```python
app.run(port=5001)  # Change from 5000
```

**Change Frontend Port:**
Edit `frontend/package.json`:
```json
"start": "PORT=3001 react-scripts start"
```

---

## ✅ File Permissions

### Check if files are readable

**Windows:**
```bash
dir /s *.py
dir /s *.jsx
```

**Linux/Mac:**
```bash
ls -la *.py
ls -la *.jsx
```

Should show all files with read permissions (r)

### If permission denied

**Linux/Mac:**
```bash
chmod +x app.py
chmod +x main.py
chmod +x setup-unix.sh
```

---

## ✅ Database & Model Files

After running `python main.py`:

```bash
# Check generated files
ls -la model.pkl
ls -la vectorizer.pkl
```

Expected: Both files exist and are > 1MB

If missing:
1. Run `python main.py` again
2. Check for errors in output
3. Verify mail_data.csv exists

---

## ✅ Browser Compatibility

Tested & working on:
- ✓ Chrome/Chromium 90+
- ✓ Firefox 88+
- ✓ Safari 14+
- ✓ Edge 90+
- ✓ Mobile Safari (iOS 14+)
- ✓ Chrome Mobile (Android 10+)

If UI issues:
1. Clear browser cache (Ctrl+Shift+Delete)
2. Hard refresh (Ctrl+Shift+R)
3. Try different browser

---

## ✅ Common Setup Issues

### Issue: ModuleNotFoundError

```bash
ModuleNotFoundError: No module named 'flask'
```

**Fix:**
```bash
pip install -r requirements.txt
pip install flask flask-cors
```

### Issue: Port 5000 in use

```bash
OSError: [Errno 98] Address already in use
```

**Fix:**
```bash
# Find process using port 5000
lsof -i :5000
# Kill it
kill -9 <PID>
# Or use different port in app.py
```

### Issue: npm install fails

```bash
npm ERR! code ERESOLVE
```

**Fix:**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install --legacy-peer-deps
```

### Issue: Model not loading

```bash
FileNotFoundError: model.pkl not found
```

**Fix:**
```bash
# Train model first
python main.py
# Check files exist
ls -la *.pkl
```

---

## ✅ Performance Baseline

After setup, verify performance:

| Metric | Target | Actual |
|--------|--------|--------|
| API Response | < 100ms | _____ |
| Frontend Load | < 2s | _____ |
| Model Accuracy | > 95% | _____ |

Run test:
```bash
python test_api.py
```

---

## ✅ Security Verification

- [ ] CORS configured
- [ ] Input validation enabled
- [ ] Error messages don't expose paths
- [ ] No debug mode in production
- [ ] Environment variables not exposed
- [ ] Model files not accessible via web

---

## ✅ Backup & Restore

### Create backup

```bash
# Backup trained models
cp model.pkl model.pkl.backup
cp vectorizer.pkl vectorizer.pkl.backup
```

### Restore from backup

```bash
# If models corrupted
cp model.pkl.backup model.pkl
cp vectorizer.pkl.backup vectorizer.pkl
```

---

## ✅ Deployment Checklist

Before deploying:

- [ ] All tests pass (`python test_api.py`)
- [ ] Frontend builds (`npm run build`)
- [ ] Model trained (`model.pkl` exists)
- [ ] No error messages
- [ ] Response times acceptable
- [ ] CORS configured
- [ ] Environment variables set
- [ ] Backups created

---

## ✅ Final Verification Script

Run this to verify everything:

```bash
# Complete verification
echo "Checking Python..."
python --version

echo "Checking Node..."
node --version

echo "Checking files..."
ls -la app.py main.py model.pkl vectorizer.pkl

echo "Checking frontend..."
ls -la frontend/src/App.jsx

echo "Testing API..."
python test_api.py

echo "All checks complete!"
```

---

## 📝 Sign-Off Checklist

- [ ] All files present and readable
- [ ] Python & Node.js installed
- [ ] Dependencies installed
- [ ] Model trained
- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] API endpoints respond correctly
- [ ] Frontend UI displays correctly
- [ ] Tests pass
- [ ] Performance acceptable
- [ ] Ready for use/deployment

---

**Setup Verification Complete! ✅**

If any checks fail, see the "Common Issues" section above.

For more help, see:
- SETUP.md - Detailed setup
- QUICK_START.md - Quick reference
- API_TESTING.md - Testing guide
