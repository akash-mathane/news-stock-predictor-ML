import pandas as pd
import os

# Load cleaned news
df_news = pd.read_csv("data/news/All_News_Cleaned.csv")
df_news["date"] = pd.to_datetime(df_news["date"], errors='coerce').dt.date

# Choose a stock
stock_file = "data/stocks/cleaned/AAPL.csv"
stock_name = "AAPL"

# Load cleaned stock
df_stock = pd.read_csv(stock_file)
df_stock["date"] = pd.to_datetime(df_stock["date"], errors='coerce').dt.date

# Merge on 'date'
df_merged = pd.merge(df_news, df_stock, on="date", how="inner")

# OPTIONAL: Create target label (price up/down)
df_merged["price_diff"] = df_merged["close"].diff()
df_merged["target"] = (df_merged["price_diff"] > 0).astype(int)

# Drop NA caused by diff()
df_merged.dropna(subset=["price_diff"], inplace=True)

# Save
output_file = f"data/merged/{stock_name}_merged.csv"
df_merged.to_csv(output_file, index=False)
print(f"✅ Merged {len(df_merged)} records to {output_file}")
