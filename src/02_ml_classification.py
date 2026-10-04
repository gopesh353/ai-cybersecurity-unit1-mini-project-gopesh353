"""Task 3: ML-Based Threat Classification (Decision Tree)."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("data/cybersecurity_dataset.csv")

# Preprocess: handle missing values, normalize numbers
df = df.fillna(df.median(numeric_only=True))  # fill missing with median

X = df.drop("label", axis=1)
y = df["label"]

# Normalize numerical attributes
num_cols = ["login_attempts", "failed_logins", "bytes_transferred", "phishing_score"]
scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy :", round(accuracy_score(y_test, pred), 3))
print("Precision:", round(precision_score(y_test, pred), 3))
print("Recall   :", round(recall_score(y_test, pred), 3))
print("F1-score :", round(f1_score(y_test, pred), 3))
