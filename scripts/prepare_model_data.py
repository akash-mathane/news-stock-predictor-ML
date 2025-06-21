import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the engineered dataset
df = pd.read_csv("data/merged/AAPL_features.csv")

# Drop columns not needed for training
drop_cols = ["date", "headline", "close", "open", "price_diff"]
df = df.drop(columns=[col for col in drop_cols if col in df.columns])

# Separate features and labels
X = df.drop("target", axis=1)
y = df["target"]

print("\U0001F4CA Features shape:", X.shape)
print("\U0001F3AF Labels shape:", y.shape)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=True, random_state=42
)

# Normalize numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save preprocessed datasets
pd.DataFrame(X_train_scaled, columns=X.columns).to_csv("data/merged/X_train.csv", index=False)
pd.DataFrame(X_test_scaled, columns=X.columns).to_csv("data/merged/X_test.csv", index=False)
pd.DataFrame(y_train).to_csv("data/merged/y_train.csv", index=False)
pd.DataFrame(y_test).to_csv("data/merged/y_test.csv", index=False)

print("\u2705 Training and test data saved!")

# Optional: Check class balance
print("Train Label Balance:")
print(y_train.value_counts(normalize=True))
print("Test Label Balance:")
print(y_test.value_counts(normalize=True))
