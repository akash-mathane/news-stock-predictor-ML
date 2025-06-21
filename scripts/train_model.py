import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

# Load data
X_train = pd.read_csv("data/merged/X_train.csv")
X_test = pd.read_csv("data/merged/X_test.csv")
y_train = pd.read_csv("data/merged/y_train.csv").squeeze()
y_test = pd.read_csv("data/merged/y_test.csv").squeeze()

print("✅ Data loaded:")
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate model
print("\U0001F4C8 Classification Report:")
print(classification_report(y_test, y_pred))
print("\U0001F4BE Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\U0001F3AF Precision:", precision_score(y_test, y_pred))
print("\U0001F501 Recall:", recall_score(y_test, y_pred))

# Feature importance plot
os.makedirs("reports/eda", exist_ok=True)
feature_importance = pd.Series(model.feature_importances_, index=X_train.columns)
feature_importance.nlargest(10).plot(kind='barh', figsize=(8, 6))
plt.title("Top 10 Feature Importances")
plt.tight_layout()
plt.savefig("reports/eda/feature_importance.png")
plt.show()

# Save the model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/random_forest_stock_predictor.pkl")
print("✅ Model saved!")
