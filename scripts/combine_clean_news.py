import pandas as pd
import glob
import os

# Path to your news data
news_path = "data/news/"
output_file = "data/news/All_News_Cleaned.csv"

# Find all .csv files in the news folder
all_files = glob.glob(os.path.join(news_path, "*.csv"))

# List to collect DataFrames
dfs = []

for file in all_files:
    try:
        df = pd.read_csv(file)

        # Clean column names
        df.columns = df.columns.str.lower()

        # Handle different file types
        if "title" in df.columns and "publishedat" in df.columns:
            df = df[["publishedat", "title"]]
            df.rename(columns={"publishedat": "date", "title": "headline"}, inplace=True)
        elif "date" in df.columns and "top1" in df.columns:  # Kaggle RedditNews format
            df["headline"] = df["top1"]  # just use Top1 as sample
            df = df[["date", "headline"]]

        # Convert date
        df["date"] = pd.to_datetime(df["date"]).dt.date

        # Drop nulls and duplicates
        df.dropna(subset=["headline"], inplace=True)
        df.drop_duplicates(inplace=True)

        dfs.append(df)

    except Exception as e:
        print(f"Error reading {file}: {e}")

# Combine all news into one DataFrame
df_all_news = pd.concat(dfs, ignore_index=True)
df_all_news.sort_values("date", inplace=True)

# Save to file
df_all_news.to_csv(output_file, index=False)
print(f"✅ Combined {len(df_all_news)} news items into {output_file}")
