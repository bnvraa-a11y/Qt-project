"""
Currency Converter Application
A PyQt6-based currency converter for Turkish Lira to USD conversion
"""
import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow


def main():
    """Initialize and run the application"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
