import pandas as pd
import os
import glob

input_dir = "data/stocks/"
output_dir = "data/stocks/cleaned/"
os.makedirs(output_dir, exist_ok=True)

# Get all stock CSVs
files = glob.glob(os.path.join(input_dir, "*.csv"))

for file in files:
    try:
        df = pd.read_csv(file)

        # Normalize column names
        df.columns = df.columns.str.strip().str.lower()

        # Keep only relevant columns
        df = df[["date", "open", "close", "volume"]]

        # Convert date
        df["date"] = pd.to_datetime(df["date"]).dt.date

        # Remove rows with missing values or duplicates
        df.dropna(inplace=True)
        df.drop_duplicates(subset="date", inplace=True)

        # Save cleaned version
        stock_name = os.path.basename(file)
        df.to_csv(os.path.join(output_dir, stock_name), index=False)
        print(f"✅ Cleaned: {stock_name} — {len(df)} rows")

    except Exception as e:
        print(f"❌ Error with {file}: {e}")
