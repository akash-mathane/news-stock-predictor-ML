import yfinance as yf
import pandas as pd
import os

# Set ticker and date range to match RedditNews (2008-08-08 to 2016-07-01)
ticker = 'AAPL'
start_date = '2008-08-08'
end_date = '2016-07-01'

# Download data
df = yf.download(ticker, start=start_date, end=end_date)

# Reset index to get 'Date' as a column
df = df.reset_index()

# Keep only required columns and rename
stock = df[['Date', 'Open', 'Close', 'Volume']].copy()
stock.columns = ['date', 'open', 'close', 'volume']

# Save cleaned stock data
os.makedirs('data/stocks/cleaned', exist_ok=True)
stock.to_csv('data/stocks/cleaned/AAPL.csv', index=False)
print(f"✅ Downloaded and saved {len(stock)} rows to data/stocks/cleaned/AAPL.csv")
