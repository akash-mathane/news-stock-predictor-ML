from textblob import TextBlob
import pandas as pd

# Load wrangled data
df = pd.read_csv("data/merged/AAPL_wrangle.csv")

# Sentiment features from headlines
df['sentiment_polarity'] = df['headline'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['sentiment_subjectivity'] = df['headline'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)

# Price-based features
df['return'] = (df['close'] - df['open']) / df['open']
df['rolling_close_3'] = df['close'].rolling(window=3).mean()
df['rolling_volatility_3'] = df['close'].rolling(window=3).std()
df['close_lag_1'] = df['close'].shift(1)

# Only drop rows where rolling features or lag are NaN
rolling_cols = ['rolling_close_3', 'rolling_volatility_3', 'close_lag_1']
df.dropna(subset=rolling_cols, inplace=True)

# Time-based features
df["date"] = pd.to_datetime(df["date"])
df['dayofweek'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df['is_month_start'] = df['date'].dt.is_month_start.astype(int)
df['is_month_end'] = df['date'].dt.is_month_end.astype(int)

# Save final feature-engineered dataset
df.to_csv("data/merged/AAPL_features.csv", index=False)
print("✅ Final feature file saved!")
print(f"Rows after feature engineering: {df.shape[0]}")
