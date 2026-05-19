from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QDoubleSpinBox, QLineEdit
)
from PySide6.QtCore import QObject, Signal, Slot, QThread
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from currency_converter import CurrencyConverter


class ConverterWorker(QObject):
    finished = Signal(float)

    def __init__(self, converter, from_curr, to_curr):
        super().__init__()
        self.converter = converter
        self.from_curr = from_curr
        self.to_curr = to_curr

    @Slot()
    def run(self):
        rate = self.converter.get_rate(self.from_curr, self.to_curr)
        self.finished.emit(rate)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.converter = CurrencyConverter()
        self.is_dark = False
        self.currencies = ["USD", "EUR", "TRY", "GBP", "JPY", "SAR", "AED"]

        self.setWindowTitle("Basic Converter")
        self.setMinimumSize(400, 300)

        self.theme_btn = QPushButton("🌙 Toggle Theme")
        self.theme_btn.clicked.connect(self.toggle_theme)

        self.amount_input = QDoubleSpinBox()
        self.amount_input.setMaximum(999999.0)
        self.amount_input.setValue(100.0)

        self.from_box = QComboBox()
        self.from_box.addItems(self.currencies)

        self.to_box = QComboBox()
        self.to_box.addItems(self.currencies)
        self.to_box.setCurrentText("TRY")

        self.result = QLineEdit()
        self.result.setReadOnly(True)

        self.convert_btn = QPushButton("Convert")
        self.convert_btn.clicked.connect(self.convert)

        layout = QVBoxLayout()
        layout.addWidget(self.theme_btn)

        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Amount:"))
        row1.addWidget(self.amount_input)
        row1.addWidget(self.from_box)
        layout.addLayout(row1)

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Result:"))
        row2.addWidget(self.result)
        row2.addWidget(self.to_box)
        layout.addLayout(row2)

        layout.addWidget(self.convert_btn)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        self.apply_theme()

    def convert(self):
        self.result.setText("Loading...")
        self.repaint()
        self.convert_btn.setEnabled(False)

        from_curr = self.from_box.currentText()
        to_curr = self.to_box.currentText()

        self._thread = QThread()
        self._worker = ConverterWorker(self.converter, from_curr, to_curr)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.finished.connect(self._on_rate)
        self._worker.finished.connect(self._thread.quit)
        self._thread.start()

    def _on_rate(self, rate: float):
        amt = self.amount_input.value()
        if rate == 0.0:
            self.result.setText("Error fetching rate!")
        else:
            self.result.setText(f"{amt * rate:.2f}")
        self.convert_btn.setEnabled(True)
        self._worker.deleteLater()
        self._thread.deleteLater()

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.apply_theme()

    def apply_theme(self):
        if self.is_dark:
            style = """
                QWidget { background: #222; color: #FFF; font-size: 14px; }
                QPushButton, QComboBox, QDoubleSpinBox, QLineEdit { 
                    background: #444; border: 1px solid #666; padding: 8px; border-radius: 4px;
                }
                QPushButton { background: #555; }
                QPushButton:hover { background: #666; }
            """
        else:
            style = """
                QWidget { background: #F5F5F5; color: #000; font-size: 14px; }
                QPushButton, QComboBox, QDoubleSpinBox, QLineEdit { 
                    background: #FFF; border: 1px solid #CCC; padding: 8px; border-radius: 4px;
                }
                QPushButton { background: #E0E0E0; }
                QPushButton:hover { background: #D0D0D0; }
            """
        self.setStyleSheet(style)
