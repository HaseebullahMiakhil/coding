import requests
import pandas as pd

def fetch_stock_price(symbol, api_key):
    try:
        # Alpha Vantage API URL for getting stock prices
        url = f'https://www.alphavantage.co/query'
        params = {
            'function': 'TIME_SERIES_INTRADAY',  # For current stock prices
            'symbol': symbol,
            'interval': '1min',  # You can change this to '5min', '15min', etc.
            'apikey': api_key
        }

        # Send a GET request to the API
        response = requests.get(url, params=params)
        data = response.json()

        # Check for an error in the response
        if 'Error Message' in data:
            print(f"Error fetching data for {symbol}: {data['Error Message']}")
            return None

        # Extracting the latest stock price from the response
        time_series = data['Time Series (1min)']
        latest_time = sorted(time_series.keys())[0]  # Get the most recent entry
        latest_data = time_series[latest_time]
        price = latest_data['1. open']  # Fetch the opening price

        return price

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Replace with your own Alpha Vantage API key
    api_key = 'YOUR_ALPHAVANTAGE_API_KEY'

    # Stock symbol you want to fetch
    stock_symbol = input("Enter the stock symbol (e.g., TSLA): ").upper()

    # Fetching the stock price
    price = fetch_stock_price(stock_symbol, api_key)

    if price is not None:
        print(f"The current stock price of {stock_symbol} is: ${price}")