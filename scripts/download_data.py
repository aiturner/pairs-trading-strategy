import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# List of S&P 100 stocks (tickers)
tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'JPM', 'V', 'WMT',
    'PG', 'JNJ', 'UNH', 'HD', 'DIS', 'MA', 'BAC', 'NFLX', 'ADBE', 'CRM',
    'KO', 'PFE', 'TMO', 'ABT', 'NKE', 'COST', 'CVX', 'WFC', 'LLY', 'MRK',
    'PEP', 'TXN', 'QCOM', 'INTC', 'AMGN', 'CMCSA', 'MCD', 'UPS', 'HON', 'IBM',
    'CAT', 'GE', 'RTX', 'LMT', 'GS', 'SPGI', 'BLK', 'AXP', 'PLD', 'DE',
    'TGT', 'LOW', 'UNP', 'NEE', 'DUK', 'MO', 'PM', 'MMM', 'CSX', 'DHR',
    'ABBV', 'ACN', 'AMD', 'BA', 'BK', 'BX', 'C', 'CHTR', 'CL', 'COP',
    'CVS', 'DD', 'ELV', 'EMR', 'F', 'FDX', 'GD', 'GILD', 'GM', 'HCA',
    'HUM', 'INTU', 'ISRG', 'LRCX', 'MDT', 'MET', 'MU', 'ORCL', 'REGN', 'SCHW'
]

# Download data for last 5 years
end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)

print("Downloading data")
data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')
data.to_csv('data/all_stocks.csv')
print(f"Data saved to data/all_stocks.csv")

for ticker in tickers:
    try:
        ticker_data = data[ticker]
        if not ticker_data.empty:
            ticker_data.to_csv(f'data/{ticker}.csv')
    except:
        pass

print(f"Downloaded data for {len(tickers)} stocks.")
