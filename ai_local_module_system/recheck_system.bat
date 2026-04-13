@echo off
echo ==============================
echo AI SYSTEM HEALTH CHECK START
echo ==============================

:: Check Python
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python not found
    pause
    exit /b
)

:: Check Storage Path
set STORAGE=C:\ai_storage
if not exist %STORAGE% (
    echo [WARNING] Storage not found, creating...
    mkdir %STORAGE%
)

:: Create subfolders
for %%f in (data models modules experience logs) do (
    if not exist %STORAGE%\%%f (
        echo Creating %%f folder...
        mkdir %STORAGE%\%%f
    )
)

:: Check venv
if not exist venv (
    echo [WARNING] venv not found
) else (
    echo venv OK
)

:: Check required files
for %%f in (start_training.py core\ai_core_kernel.py core\storage_manager.py) do (
    if not exist %%f (
        echo [ERROR] Missing %%f
    ) else (
        echo Found %%f
    )
)

echo ==============================
echo SYSTEM CHECK COMPLETE
echo ==============================
pause
