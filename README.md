# News Sentiment Analysis and Stock Movement Predictor

This project predicts stock price movement using news sentiment analysis. Below is a detailed step-by-step guide of the entire workflow, from data collection to model training and evaluation.

---

## Project Structure
- `data/` - Raw and processed datasets
  - `news/` - News articles (RedditNews, NewsAPI, etc.)
  - `stocks/` - Stock price data (raw and cleaned)
  - `merged/` - Combined and feature-engineered datasets
- `notebooks/` - Jupyter notebooks for stepwise development
- `scripts/` - Python scripts for data collection, cleaning, merging, feature engineering, and modeling
- `models/` - Saved models
- `reports/` - EDA, metrics, and feature importance plots
- `config/` - API keys and settings

---

## Step-by-Step Workflow

### PHASE 1: Project Setup
1. **Create folders and files** as per the structure above.
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your NewsAPI key** to `config/newsapi_key.txt`.

---

### PHASE 2: Data Collection & Preparation

#### 2.1 Download News Data
- Download RedditNews from Kaggle and/or use NewsAPI to fetch news for specific companies/dates.
- Place all news CSVs in `data/news/`.
- Example script: `scripts/download_news_data.py`

#### 2.2 Download Stock Data
- Download historical stock data using yfinance for the same date range as your news data.
- Save cleaned stock CSVs in `data/stocks/cleaned/`.
- Example script: `scripts/download_historical_stock_data.py`

#### 2.3 Combine & Clean News Files
- Combine all news CSVs, normalize columns, convert dates, and save as `data/news/All_News_Cleaned.csv`.
- Script: `scripts/combine_clean_news.py`

#### 2.4 Clean Stock Data
- Normalize columns, keep only `date`, `open`, `close`, `volume`, and save to `data/stocks/cleaned/`.
- Script: `scripts/clean_stock_data.py`

#### 2.5 Merge News + Stock Data
- Merge news and stock data on `date`.
- Create target label (price up/down) and save as `data/merged/AAPL_merged.csv`.
- Script: `scripts/merge_news_stock.py`

---

### PHASE 3: Data Wrangling
- Clean merged data: handle missing values, remove duplicates, aggregate headlines per day, and save as `data/merged/AAPL_wrangle.csv`.
- Script: `scripts/wrangle_merged_data.py`

---

### PHASE 4: Feature Engineering
- Extract sentiment features from headlines using TextBlob.
- Create price-based features (returns, rolling averages, volatility, lag features).
- Add time-based features (day of week, month, etc.).
- Save as `data/merged/AAPL_features.csv`.
- Script: `scripts/feature_engineering.py`

---

### PHASE 5: Modeling Preparation
- Split features and labels, train-test split, scale features, and save as `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv` in `data/merged/`.
- Script: `scripts/prepare_model_data.py`

---

### PHASE 6: Modeling
- Train a Random Forest classifier on the training data.
- Evaluate using accuracy, precision, recall, F1, and confusion matrix.
- Visualize feature importances and save the plot to `reports/eda/feature_importance.png`.
- Save the trained model to `models/random_forest_stock_predictor.pkl`.
- Script: `scripts/train_model.py`

---

## Example Pipeline Run
1. Download and clean news and stock data.
2. Merge and wrangle data.
3. Engineer features.
4. Prepare data for modeling.
5. Train and evaluate the model.

---

## Tips
- Always ensure your news and stock data cover the same date range.
- Use the debug script `scripts/debug_data_pipeline.py` to check row counts and date overlaps at each step.
- Adjust scripts as needed for other stocks or news sources.

---

## Credits
- NewsAPI, Kaggle RedditNews, Yahoo Finance (yfinance), TextBlob, scikit-learn, matplotlib, seaborn.

---

## Usage
Run scripts in `scripts/` sequentially or follow notebooks in `notebooks/` for stepwise development.

---

For any issues or questions, please refer to the scripts or open an issue.
