import pandas as pd
import os

files = [
    "data/news/All_News_Cleaned.csv",
    "data/stocks/cleaned/AAPL.csv",
    "data/merged/AAPL_merged.csv",
    "data/merged/AAPL_wrangle.csv",
    "data/merged/AAPL_features.csv"
]

def print_unique_dates(file, col_name):
    if os.path.exists(file):
        try:
            df = pd.read_csv(file)
            if col_name in df.columns:
                dates = pd.to_datetime(df[col_name], errors='coerce').dt.date
                print(f"{file}: {len(dates.unique())} unique dates, sample: {list(dates.dropna().unique())[:5]}")
            else:
                print(f"{file}: No '{col_name}' column found.")
        except Exception as e:
            print(f"{file}: Error reading file: {e}")
    else:
        print(f"{file}: File does not exist.")

for f in files:
    if os.path.exists(f):
        try:
            df = pd.read_csv(f)
            print(f"{f}: {df.shape[0]} rows, {df.shape[1]} columns")
            print(df.head(2))
        except Exception as e:
            print(f"{f}: Error reading file: {e}")
    else:
        print(f"{f}: File does not exist.")

# Print unique dates for news and stock files
print_unique_dates("data/news/All_News_Cleaned.csv", "date")
print_unique_dates("data/stocks/cleaned/AAPL.csv", "date")
