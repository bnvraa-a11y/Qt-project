@echo off
REM Configure and run Currency Converter in Qt Creator
REM This creates the necessary build directory structure

echo ========================================
echo Currency Converter - Qt Creator Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo [✓] Python found
echo.

REM Install requirements
echo Installing dependencies...
python -m pip install --quiet PyQt6 requests
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [✓] Dependencies installed
echo.

REM Create build directory
if not exist build (
    mkdir build
    echo [✓] Build directory created
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Open Qt Creator
echo 2. File → Open File or Project
echo 3. Select: CurrencyConverter.pro
echo 4. Projects → Run
echo 5. Set Executable to: python
echo 6. Set Arguments to: main.py
echo 7. Press Ctrl+R to run
echo.
pause
