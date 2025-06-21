import pandas as pd

# Load merged data
df = pd.read_csv("data/merged/AAPL_merged.csv")
print(f"Loaded: {df.shape[0]} rows")
print(df.columns)
print(df.head(3))

# Drop rows with missing headline or prices
before = df.shape[0]
df.dropna(subset=["headline", "close", "open"], inplace=True)
print(f"After dropna (headline, close, open): {df.shape[0]} rows (dropped {before - df.shape[0]})")

# Remove duplicates
before = df.shape[0]
df.drop_duplicates(subset=["date", "headline"], inplace=True)
print(f"After drop_duplicates: {df.shape[0]} rows (dropped {before - df.shape[0]})")

# Remove rows with extreme price_diff values (optional, adjust threshold as needed)
if 'price_diff' in df.columns:
    before = df.shape[0]
    df = df[df['price_diff'].abs() < 100]
    print(f"After removing extreme price_diff: {df.shape[0]} rows (dropped {before - df.shape[0]})")

# Truncate long headlines (optional)
df['headline'] = df['headline'].astype(str).str.slice(0, 300)

# Group all headlines per day into one big string
df_grouped = df.groupby("date").agg({
    "headline": lambda x: " ".join(x),
    "open": "first",
    "close": "first",
    "volume": "first",
    "price_diff": "first" if 'price_diff' in df.columns else (lambda x: None),
    "target": "first" if 'target' in df.columns else (lambda x: None)
}).reset_index()

print(f"After grouping: {df_grouped.shape[0]} rows")

# Save the cleaned dataset
output_file = "data/merged/AAPL_wrangle.csv"
df_grouped.to_csv(output_file, index=False)
print(f"✅ Saved clean file: {output_file}")

# Test & Validate
if 'target' in df_grouped.columns:
    print(df_grouped["target"].value_counts())
print(df_grouped.isnull().sum())
