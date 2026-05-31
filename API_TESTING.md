# API Testing Guide - Spam Detection Service

## 🧪 Automated Testing

Run the comprehensive test suite:

```bash
# Test with default API URL (http://localhost:5000)
python test_api.py

# Test with custom URL
python test_api.py http://your-api-url:port
```

## 🔧 Manual Testing

### Using cURL

#### 1. Check API Status
```bash
curl http://localhost:5000/
```

#### 2. Health Check
```bash
curl http://localhost:5000/api/health
```

#### 3. Single Message Prediction
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Congratulations! You won a free iPhone. Click here now."
  }'
```

#### 4. Batch Prediction
```bash
curl -X POST http://localhost:5000/api/batch-predict \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      "Free money! Click here",
      "Hi, how are you?",
      "Claim your prize now!"
    ]
  }'
```

### Using Python

```python
import requests

BASE_URL = "http://localhost:5000"

# Single prediction
response = requests.post(
    f"{BASE_URL}/api/predict",
    json={"message": "Free iPhone! Click now"}
)
print(response.json())

# Batch prediction
response = requests.post(
    f"{BASE_URL}/api/batch-predict",
    json={
        "messages": [
            "Congratulations!",
            "Hi there",
            "You won!"
        ]
    }
)
print(response.json())
```

### Using JavaScript/Fetch

```javascript
const BASE_URL = "http://localhost:5000";

// Single prediction
async function predictMessage(message) {
  const response = await fetch(`${BASE_URL}/api/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });
  return await response.json();
}

// Test
predictMessage("Free money!").then(console.log);
```

### Using Postman

1. **New Request** → POST
2. **URL**: `http://localhost:5000/api/predict`
3. **Headers**:
   ```
   Content-Type: application/json
   ```
4. **Body** (raw JSON):
   ```json
   {
     "message": "Congratulations! You won!"
   }
   ```
5. **Send**

## 📊 Expected Response Examples

### Success Response (SPAM)
```json
{
  "status": "success",
  "prediction": "spam",
  "label": "🚨 SPAM",
  "confidence": 97.5,
  "message": "Congratulations! You won a free iPhone...",
  "timestamp": "2026-05-31T10:30:00.123456"
}
```

### Success Response (HAM)
```json
{
  "status": "success",
  "prediction": "ham",
  "label": "✅ SAFE MESSAGE",
  "confidence": 98.2,
  "message": "Hi, how are you doing?",
  "timestamp": "2026-05-31T10:30:00.123456"
}
```

### Error Response
```json
{
  "status": "error",
  "message": "Message cannot be empty"
}
```

## ✅ Test Cases

### Valid Inputs
- ✓ Single spam message
- ✓ Single ham message
- ✓ Multiple messages (batch)
- ✓ Long messages (up to 10,000 chars)
- ✓ Messages with special characters
- ✓ Messages in different languages

### Invalid Inputs
- ✗ Empty message
- ✗ Missing message field
- ✗ Message exceeds 10,000 characters
- ✗ Invalid JSON
- ✗ Empty batch

### Performance Tests
- Response time: < 100ms per message
- Batch processing: up to 100 messages
- Concurrent requests: supported

## 🚀 Performance Benchmarks

```
Single Prediction:   ~50ms
Batch (10 messages): ~120ms
Batch (100 messages): ~800ms
Memory Usage: ~150MB
```

## 🔍 Debugging

### Enable Debug Mode

**Backend (Python):**
```python
# In app.py
app.run(debug=True)  # Shows detailed error messages
```

### Check Logs

```bash
# Monitor Flask logs
# Look for: - - [timestamp] "POST /api/predict HTTP/1.1" 200

# Monitor with verbose output
curl -v http://localhost:5000/api/predict
```

### Common Issues

#### Connection Refused
```
Error: Cannot connect to http://localhost:5000
Solution: Make sure Flask backend is running
  python app.py
```

#### Model Not Found
```
Error: "Model not loaded"
Solution: Train the model first
  python main.py
```

#### JSON Parse Error
```
Error: Invalid JSON in request
Solution: Ensure JSON is properly formatted
  Use: -H "Content-Type: application/json"
```

## 📈 Load Testing

### Using Apache Bench
```bash
# Single request
ab -n 100 -c 10 -T application/json \
  -p payload.json http://localhost:5000/api/predict

# Where payload.json contains:
# {"message": "Test message"}
```

### Using wrk
```bash
# Download: https://github.com/wg/wrk

wrk -t4 -c100 -d30s \
  -s script.lua \
  http://localhost:5000/api/predict
```

## 🔐 Security Testing

- [x] Input validation
- [x] Message length limits
- [x] CORS enabled
- [x] Error handling
- [x] No sensitive data in responses

## 📝 Test Report Template

```markdown
# Test Report - Spam Detection API

Date: [DATE]
Tester: [NAME]
Environment: [DEV/STAGING/PROD]

## Test Results

### Functionality
- [x] API Connection
- [x] Single Prediction
- [x] Batch Prediction
- [x] Health Check
- [x] Error Handling

### Performance
- Response Time: ___ms
- Throughput: ___req/s
- Error Rate: ___%

### Issues Found
1. [Issue Description]
   - Severity: [High/Medium/Low]
   - Status: [Open/Closed]

## Conclusion
[PASS/FAIL]
```

---

For more information, see [SETUP.md](SETUP.md)
