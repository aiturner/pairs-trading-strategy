import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time

print("=" * 60)
print("DOWNLOADING REAL S&P 100 DATA")
print("(VPN should be active)")
print("=" * 60)

# S&P 100 stocks (the most liquid, good for pairs trading)
tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'JPM', 'V', 'WMT',
    'PG', 'JNJ', 'UNH', 'HD', 'DIS', 'MA', 'BAC', 'NFLX', 'ADBE', 'CRM',
    'KO', 'PFE', 'TMO', 'ABT', 'NKE', 'COST', 'CVX', 'WFC', 'LLY', 'MRK',
    'PEP', 'TXN', 'QCOM', 'INTC', 'AMGN', 'CMCSA', 'MCD', 'UPS', 'HON', 'IBM',
    'CAT', 'GE', 'RTX', 'LMT', 'GS', 'AXP', 'DE', 'TGT', 'LOW', 'UNP'
]

end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)

print(f"📅 Downloading 5 years of data ({start_date.date()} to {end_date.date()})")
print(f"📊 {len(tickers)} stocks")
print()

all_data = {}

for i, ticker in enumerate(tickers, 1):
    print(f"[{i}/{len(tickers)}] Downloading {ticker}...", end=" ")
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date)
        if not hist.empty:
            all_data[ticker] = hist
            print(f"✅ {len(hist)} rows")
        else:
            print(f"⚠️ No data")
        time.sleep(0.3)  # Be gentle with Yahoo
    except Exception as e:
        print(f"❌ Error: {str(e)[:50]}")

print()
print("=" * 60)
print("SAVING DATA")
print("=" * 60)

# Save individual files
for ticker, df in all_data.items():
    df.to_csv(f'data/{ticker}.csv')
    print(f"   💾 {ticker}.csv")

# Save combined (multi-level columns)
if all_data:
    combined = pd.concat(all_data, axis=1)
    combined.to_csv('data/all_stocks_real.csv')
    print(f"   💾 all_stocks_real.csv")

print()
print(f"✅ COMPLETE! Downloaded {len(all_data)}/{len(tickers)} stocks")
print(f"📁 Data saved in 'data/' folder")
print("=" * 60)
