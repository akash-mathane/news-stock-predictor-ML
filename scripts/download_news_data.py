# Download news data script
import requests
import pandas as pd
import os
from datetime import datetime

# Load API Key
with open("config/newsapi_key.txt", "r") as file:
    API_KEY = file.read().strip()

# Config
company = "Apple"
query_date = "2023-12-01"
url = (
    f"https://newsapi.org/v2/everything?q={company}"
    f"&from={query_date}&sortBy=publishedAt&language=en&apiKey={API_KEY}"
)

# API Request
response = requests.get(url)
data = response.json()

# Extract Articles
articles = data.get("articles", [])
# Safely extract publishedAt, title, and source name
rows = []
for article in articles:
    rows.append({
        "publishedAt": article.get("publishedAt"),
        "title": article.get("title"),
        "source": article.get("source", {}).get("name")
    })
df_news = pd.DataFrame(rows)

# Only convert publishedAt if DataFrame is not empty and column exists
if not df_news.empty and 'publishedAt' in df_news.columns:
    df_news['publishedAt'] = pd.to_datetime(df_news['publishedAt'])

# Save
os.makedirs("data/news", exist_ok=True)
filename = f"data/news/{company}_{query_date}.csv"
df_news.to_csv(filename, index=False)

print(f"Saved {len(df_news)} articles to {filename}")
