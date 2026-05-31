@echo off
REM Spam Detection Website - Quick Start Script for Windows

echo.
echo ================================
echo  Spam Detection Quick Start
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org
    pause
    exit /b 1
)

echo [1/5] Training ML model...
python main.py
if errorlevel 1 (
    echo ERROR: Model training failed
    pause
    exit /b 1
)

echo.
echo [2/5] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install Python packages
    pause
    exit /b 1
)

echo.
echo [3/5] Installing React dependencies...
cd frontend
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install npm packages
    pause
    exit /b 1
)
cd ..

echo.
echo ================================
echo  Ready to Start!
echo ================================
echo.
echo Next steps:
echo.
echo Terminal 1 - Start Backend:
echo   python app.py
echo.
echo Terminal 2 - Start Frontend:
echo   cd frontend
echo   npm start
echo.
echo Then open: http://localhost:3000
echo.
pause
