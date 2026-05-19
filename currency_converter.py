import requests

class CurrencyConverter:
    def get_rate(self, from_curr, to_curr):
        if from_curr == to_curr:
            return 1.0
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
            response = requests.get(url, timeout=5)
            data = response.json()
            return data.get("rates", {}).get(to_curr, 0.0)
        except Exception:
            return 0.0
