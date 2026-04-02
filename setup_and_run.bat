@echo off
TITLE OBD AI SYSTEM - FULL SETUP & RUN

ECHO =====================================
ECHO   OBD AI SYSTEM AUTO SETUP & RUN
ECHO =====================================

:: Step 1: Check Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO Python not found! Please install Python first.
    pause
    exit
)

:: Step 2: Create Virtual Environment
IF NOT EXIST venv (
    ECHO Creating virtual environment...
    python -m venv venv
)

:: Step 3: Activate venv
call venv\Scripts\activate

:: Step 4: Install requirements
IF EXIST requirements.txt (
    ECHO Installing dependencies...
    pip install -r requirements.txt
) ELSE (
    ECHO No requirements.txt found, installing basic packages...
    pip install fastapi uvicorn
)

:: Step 5: Start Backend Server
start cmd /k "echo Starting WebSocket Server... && python -m uvicorn backend.realtime.ws_server:app --host 0.0.0.0 --port 8000"

:: Wait
TIMEOUT /T 3 >nul

:: Step 6: Start AI Engine (if exists)
IF EXIST ai_engine.py (
    start cmd /k "echo Starting AI Engine... && python ai_engine.py"
)

:: Step 7: Open browser
start http://localhost:8000/docs

ECHO =====================================
ECHO   SYSTEM READY FOR TEST #1
ECHO =====================================
pause
