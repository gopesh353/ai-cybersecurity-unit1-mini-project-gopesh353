"""Generate a simple synthetic cybersecurity dataset."""
import numpy as np
import pandas as pd

np.random.seed(42)
n = 200

login_attempts = np.random.randint(1, 11, n)
failed_logins = np.random.randint(0, 9, n)
bytes_transferred = np.random.randint(100, 10001, n)
phishing_score = np.round(np.random.rand(n), 2)
unusual_hour = np.random.choice([0, 1], n, p=[0.7, 0.3])

# Simple rule for label: suspicious if many failed logins, high phishing score, or odd-hour + many attempts
label = ((failed_logins > 3) | (phishing_score > 0.7) | ((unusual_hour == 1) & (login_attempts > 5))).astype(int)

df = pd.DataFrame({
    "login_attempts": login_attempts,
    "failed_logins": failed_logins,
    "bytes_transferred": bytes_transferred,
    "phishing_score": phishing_score,
    "unusual_hour": unusual_hour,
    "label": label,
})

# Add a few missing values to demonstrate preprocessing
df.loc[5, "phishing_score"] = None
df.loc[12, "bytes_transferred"] = None
df.loc[30, "failed_logins"] = None

df.to_csv("data/cybersecurity_dataset.csv", index=False)
print("Saved data/cybersecurity_dataset.csv with shape:", df.shape)
print(df.head())
