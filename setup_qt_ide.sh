#!/bin/bash
# Configure and run Currency Converter in Qt Creator
# This creates the necessary build directory structure

echo "========================================"
echo "Currency Converter - Qt Creator Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Please install Python from https://www.python.org"
    exit 1
fi

echo "[✓] Python found"
echo ""

# Install requirements
echo "Installing dependencies..."
python3 -m pip install --quiet PyQt6 requests

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo "[✓] Dependencies installed"
echo ""

# Create build directory
if [ ! -d "build" ]; then
    mkdir -p build
    echo "[✓] Build directory created"
fi

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Open Qt Creator"
echo "2. File → Open File or Project"
echo "3. Select: CurrencyConverter.pro"
echo "4. Projects → Run"
echo "5. Set Executable to: python3"
echo "6. Set Arguments to: main.py"
echo "7. Press Ctrl+R to run"
echo ""
