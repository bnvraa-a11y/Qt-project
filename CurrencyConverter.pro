TEMPLATE = app
TARGET = CurrencyConverter
CONFIG += c++17

QT += gui core network

# Specify the Python executable path for Qt IDE
PYTHON_VERSION = 3
PYTHON_EXECUTABLE = python

# Output directories
DESTDIR = ./bin
MOC_DIR = ./build/moc
OBJECTS_DIR = ./build/obj
RCC_DIR = ./build/rcc

# Version info
VERSION = 1.0.0
QMAKE_TARGET_COMPANY = CurrencyConverter App
QMAKE_TARGET_PRODUCT = Currency Converter
QMAKE_TARGET_DESCRIPTION = PyQt6 Currency Converter Application

# This is a PyQt6 project - use: python main.py
message("To run this PyQt6 application, execute: python main.py")

DISTFILES += \
    main.py
