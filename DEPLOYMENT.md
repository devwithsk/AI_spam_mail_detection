# Deployment Guide - Spam Detection Website

## 🚀 Deployment Options

### Quick Deployment Summary

| Platform | Backend | Frontend | Cost | Setup Time |
|----------|---------|----------|------|-----------|
| **Heroku** | ✅ | ✅ | Free/Paid | 10 min |
| **AWS** | ✅ | ✅ | Paid | 20 min |
| **DigitalOcean** | ✅ | ✅ | Paid | 15 min |
| **Netlify** | ❌ | ✅ | Free | 5 min |
| **Vercel** | ❌ | ✅ | Free | 5 min |
| **Docker** | ✅ | ✅ | Local/Cloud | 10 min |

---

## 🐳 Docker Deployment (Recommended)

### Prerequisites
- Docker installed
- Docker Hub account (optional, for pushing images)

### Build & Run Locally

```bash
# Build Docker image
docker build -t spam-detector:latest .

# Run container
docker run -p 5000:5000 spam-detector:latest
```

### Using Docker Compose (Easiest)

```bash
# Start both backend and frontend
docker-compose up -d

# Stop services
docker-compose down
```

Access:
- Frontend: http://localhost:3000
- Backend: http://localhost:5000

### Push to Docker Hub

```bash
# Tag image
docker tag spam-detector:latest YOUR_USERNAME/spam-detector:latest

# Login
docker login

# Push
docker push YOUR_USERNAME/spam-detector:latest
```

---

## ☁️ Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed

### Backend Deployment

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-spam-detector-api

# Add Procfile (already provided)
echo "web: gunicorn app:app" > Procfile

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Frontend Deployment

```bash
cd frontend

# Build optimized version
npm run build

# Install Netlify CLI
npm install -g netlify-cli

# Deploy to Netlify
netlify deploy --prod
```

---

## 🌐 AWS Deployment

### Backend on AWS EC2

```bash
# 1. Launch EC2 instance (Ubuntu 20.04)
# 2. SSH into instance
ssh -i your-key.pem ubuntu@your-instance-ip

# 3. Install dependencies
sudo apt update
sudo apt install python3-pip python3-venv nginx

# 4. Clone repo
git clone https://github.com/your-repo/spam-detector.git
cd spam-detector

# 5. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 6. Install packages
pip install -r requirements.txt
python main.py  # Train model

# 7. Install Gunicorn
pip install gunicorn

# 8. Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# 9. Configure Nginx
# Edit /etc/nginx/sites-available/default
# Point to localhost:5000
sudo systemctl restart nginx
```

### Frontend on AWS S3 + CloudFront

```bash
cd frontend

# Build
npm run build

# Install AWS CLI
pip install awscli

# Configure AWS
aws configure

# Upload to S3
aws s3 sync build/ s3://your-bucket-name

# CloudFront distribution (manual via AWS console)
```

---

## 🎈 DigitalOcean Deployment

### Prerequisites
- DigitalOcean account
- SSH access

### Using App Platform (Easiest)

1. **Connect GitHub Repo**
   - Sign into DigitalOcean
   - Go to "Apps"
   - Click "Create App"
   - Select GitHub repo

2. **Configure**
   ```yaml
   name: spam-detector
   services:
   - name: backend
     github:
       repo: your-repo
       branch: main
     source_dir: ./
     build_command: pip install -r requirements.txt && python main.py
     run_command: gunicorn -w 4 app:app
     envs:
     - key: FLASK_ENV
       value: production
     http_port: 5000
     
   - name: frontend
     github:
       repo: your-repo
       branch: main
     source_dir: ./frontend
     build_command: npm run build
     run_command: npm run start
     http_port: 3000
   ```

3. **Deploy** - Click "Create App"

---

## 🔗 Netlify Deployment (Frontend Only)

```bash
cd frontend

# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
netlify deploy --prod

# Or drag & drop build/ folder on netlify.com
```

**Environment Variables:**
```
REACT_APP_API_URL=your-backend-url
```

---

## ✅ Vercel Deployment (Frontend Only)

### Connect GitHub

1. Go to vercel.com
2. Click "Add New" → "Project"
3. Import GitHub repo
4. Set:
   - Framework: React
   - Root Directory: frontend
5. Environment: `REACT_APP_API_URL=your-backend-url`
6. Deploy

### Deploy from CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

---

## 🔧 Production Configuration

### Backend (Production)

```python
# app.py - Update these settings

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://your-frontend-url"],
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    }
})

app.run(
    debug=False,  # ⚠️ NEVER True in production
    host="0.0.0.0",
    port=5000,
    use_reloader=False
)
```

### Use Gunicorn

```bash
# Install
pip install gunicorn

# Run
gunicorn -w 4 -b 0.0.0.0:5000 --timeout 120 app:app

# With process manager (systemd)
[Unit]
Description=Spam Detector API
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/app
ExecStart=/app/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

### Frontend (Production)

```bash
# Build optimized version
npm run build

# Serve with production server
npm install -g serve
serve -s build -l 3000

# Or use Nginx
```

---

## 🔐 Security Checklist

- [ ] Remove debug mode
- [ ] Set CORS origins properly
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS/SSL
- [ ] Set strong headers (Helmet.js for Node)
- [ ] Rate limiting enabled
- [ ] Input validation
- [ ] Regular security updates

---

## 📊 Environment Variables

### Backend (.env)

```env
FLASK_ENV=production
FLASK_DEBUG=False
CORS_ORIGINS=https://your-frontend-url
MODEL_PATH=/app/model.pkl
VECTORIZER_PATH=/app/vectorizer.pkl
```

### Frontend (.env.production)

```env
REACT_APP_API_URL=https://your-backend-url
REACT_APP_VERSION=1.0.0
```

---

## 🔍 Monitoring & Logs

### Heroku
```bash
# View logs
heroku logs --tail

# View specific app
heroku logs --app your-app-name --tail
```

### AWS CloudWatch
- Monitor EC2 instances
- View application logs
- Set alarms

### DigitalOcean
- Built-in monitoring
- Logs in app console

---

## 🎯 Domain & SSL

### Custom Domain

1. **Get domain** - GoDaddy, Namecheap, etc.
2. **Point to hosting**
   - Update DNS records
   - Usually CNAME to hosting provider

### SSL Certificate

**Heroku:** Automatic (free)

**AWS:**
```bash
# Using AWS Certificate Manager
aws acm request-certificate \
  --domain-name yourdomain.com
```

**DigitalOcean:** Built-in or Let's Encrypt

---

## 📈 Scaling

### Horizontal Scaling (Multiple Servers)

```bash
# Heroku
heroku ps:scale web=2

# Docker with Nginx load balancer
docker-compose up -d --scale backend=3
```

### Caching Layer

```python
# Add Redis caching
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/api/predict')
@cache.cached(timeout=3600)
def predict():
    # ...
```

---

## ✅ Deployment Checklist

- [ ] Model trained (`model.pkl`, `vectorizer.pkl`)
- [ ] Environment variables set
- [ ] Dependencies installed
- [ ] Frontend built (`npm run build`)
- [ ] CORS configured
- [ ] SSL/HTTPS enabled
- [ ] Monitoring enabled
- [ ] Backups configured
- [ ] Team access configured

---

## 🐛 Troubleshooting Deployment

### Backend won't start
```bash
# Check logs
heroku logs -t

# Verify model files exist
ls -la *.pkl

# Reinstall dependencies
pip install -r requirements.txt
```

### Frontend shows blank page
```bash
# Check build output
npm run build

# View browser console (F12)
# Check network tab for API calls

# Verify REACT_APP_API_URL
echo $REACT_APP_API_URL
```

### API calls failing
```bash
# Check backend URL in frontend
cat frontend/.env

# Test backend directly
curl https://your-backend/api/health

# Check CORS headers
curl -H "Origin: your-frontend-url" \
     -v https://your-backend/api/predict
```

---

## 📞 Support

For deployment issues:
1. Check application logs
2. Review [SETUP.md](SETUP.md)
3. Check [API_TESTING.md](API_TESTING.md)

---

**Happy Deploying! 🚀**
