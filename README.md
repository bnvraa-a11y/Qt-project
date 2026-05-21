# Simple Currency Converter

A lightweight, single-file currency converter built with Python and PySide6. It's designed to be simple to read, easy to understand, and perfect for studying how to create basic desktop applications with Qt!

## Features
- Clean & Simple UI: Enter an amount, pick your currencies, and click convert.
- Fast: Performs instant calculations without needing to connect to the internet.
- Beginner Friendly: Written in under 150 lines of code.

## Requirements
You'll need Python installed on your computer, along with the PySide6 library. 

You can install PySide6 using pip:
pip install PySide6

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the folder where you saved currency_converter.py.
3. Run the following command:
python currency_converter.py

## Notes
- The exchange rates in this app are hardcoded into a dictionary for simplicity. If you want real-time rates for a production app, you would typically connect this to a live currency API!
- Currently supported currencies: USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, and TRY (Turkish Lira).
