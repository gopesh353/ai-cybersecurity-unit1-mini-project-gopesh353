"""Task 4: DL Prototype (MLPClassifier) vs ML (Decision Tree)."""
import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/cybersecurity_dataset.csv")
df = df.fillna(df.median(numeric_only=True))

X = df.drop("label", axis=1)
y = df["label"]

num_cols = ["login_attempts", "failed_logins", "bytes_transferred", "phishing_score"]
scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ML model
t0 = time.time()
ml = DecisionTreeClassifier(random_state=42)
ml.fit(X_train, y_train)
ml_time = time.time() - t0
ml_acc = accuracy_score(y_test, ml.predict(X_test))

# DL prototype: simple neural network (1 hidden layer, 10 neurons)
t0 = time.time()
dl = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
dl.fit(X_train, y_train)
dl_time = time.time() - t0
dl_acc = accuracy_score(y_test, dl.predict(X_test))

print(f"ML (Decision Tree): accuracy={ml_acc:.3f}, training time={ml_time:.3f}s")
print(f"DL (MLP 1x10)     : accuracy={dl_acc:.3f}, training time={dl_time:.3f}s")
print("\nFeasibility: Decision Tree is faster and simpler for this small dataset.")
print("MLP needs more data/tuning and takes longer, but can learn complex patterns.")
