@echo off
TITLE OBD AI SYSTEM - START

echo ==============================
echo Starting OBD AI System...
echo ==============================

:: Activate virtual env (if exists)
IF EXIST venv (
    call venv\Scripts\activate
)

:: Start Backend Server
start cmd /k "echo Starting Backend Server... && python -m uvicorn backend.realtime.ws_server:app --host 0.0.0.0 --port 8000"

:: Wait a bit
timeout /t 3 >nul

:: Start AI Engine (optional)
start cmd /k "echo Starting AI Engine... && python ai_engine.py"

:: Wait a bit
timeout /t 2 >nul

:: Open Dashboard (optional)
start http://localhost:8000/docs

echo ==============================
echo System Started Successfully!
echo ==============================
pause
