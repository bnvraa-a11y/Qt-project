"""
Currency Converter - Quick Start Guide

This file demonstrates how to use the Currency Converter application
"""

# Example 1: Direct currency conversion
from currency_converter import CurrencyConverter

converter = CurrencyConverter()

# Get exchange rate
success, rate, message = converter.get_exchange_rate("TRY", "USD")

if success:
    print(f"Current rate: 1 TRY = {rate:.4f} USD")
    
    # Convert amount
    amount_try = 1000
    amount_usd = converter.convert(amount_try, rate)
    print(f"{amount_try} TRY = {amount_usd:.2f} USD")
else:
    print(f"Error: {message}")


# Example 2: Validate amount
valid, amount, message = converter.validate_amount("500")
if valid:
    print(f"Valid amount: {amount}")
else:
    print(f"Invalid: {message}")
