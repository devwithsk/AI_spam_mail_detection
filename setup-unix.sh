#!/bin/bash

# Spam Detection Website - Quick Start Script for Linux/Mac

echo ""
echo "================================"
echo " Spam Detection Quick Start"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed"
    echo "Please install Node.js from https://nodejs.org"
    exit 1
fi

echo "[1/5] Training ML model..."
python3 main.py
if [ $? -ne 0 ]; then
    echo "ERROR: Model training failed"
    exit 1
fi

echo ""
echo "[2/5] Installing Python dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install Python packages"
    exit 1
fi

echo ""
echo "[3/5] Installing React dependencies..."
cd frontend
npm install
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install npm packages"
    exit 1
fi
cd ..

echo ""
echo "================================"
echo " Ready to Start!"
echo "================================"
echo ""
echo "Next steps:"
echo ""
echo "Terminal 1 - Start Backend:"
echo "  python3 app.py"
echo ""
echo "Terminal 2 - Start Frontend:"
echo "  cd frontend"
echo "  npm start"
echo ""
echo "Then open: http://localhost:3000"
echo ""
