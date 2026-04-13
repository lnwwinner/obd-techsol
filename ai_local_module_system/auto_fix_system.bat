@echo off
echo ==============================
echo AI AUTO FIX SYSTEM START
echo ==============================

:: Ensure Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python first.
    pause
    exit /b
)

:: Ensure storage
set STORAGE=C:\ai_storage
if not exist %STORAGE% (
    echo [FIX] Creating storage...
    mkdir %STORAGE%
)

for %%f in (data models modules experience logs) do (
    if not exist %STORAGE%\%%f (
        echo [FIX] Creating %%f folder...
        mkdir %STORAGE%\%%f
    )
)

:: Fix venv
if not exist venv (
    echo [FIX] Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

:: Install requirements
if exist requirements.txt (
    echo [FIX] Installing requirements...
    pip install -r requirements.txt
) else (
    echo [WARNING] requirements.txt not found
)

:: Check core files
for %%f in (start_training.py core\ai_core_kernel.py core\storage_manager.py) do (
    if not exist %%f (
        echo [ERROR] Missing %%f
    ) else (
        echo [OK] %%f
    )
)

echo ==============================
echo AUTO FIX COMPLETE
echo ==============================
pause
