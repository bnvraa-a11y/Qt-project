@echo off
REM Currency Converter Application Launcher
REM This script installs dependencies and runs the application

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Launching Currency Converter...
python main.py

pause
