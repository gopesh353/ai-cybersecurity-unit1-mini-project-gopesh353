"""Task 2: Threat Landscape Analysis (EDA + plots)."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cybersecurity_dataset.csv")

print("Shape:", df.shape)
print(df.describe())
print("\nLabel counts (0=Normal, 1=Suspicious):")
print(df["label"].value_counts())

# Common threat indicators: mean values by class
print("\nMean by class:")
print(df.groupby("label").mean(numeric_only=True))

sns.set(style="whitegrid")

# Plot 1: Normal vs Suspicious count
plt.figure()
sns.countplot(x="label", data=df)
plt.xticks([0, 1], ["Normal", "Suspicious"])
plt.title("Normal vs Suspicious Events")
plt.ylabel("Count")
plt.savefig("outputs/normal_vs_suspicious.png")
plt.close()

# Plot 2: Distribution of failed_logins by class
plt.figure()
sns.histplot(data=df, x="failed_logins", hue="label", bins=9, multiple="dodge")
plt.title("Failed Logins Distribution (Normal vs Suspicious)")
plt.savefig("outputs/failed_logins_dist.png")
plt.close()

# Plot 3: Distribution of phishing_score by class
plt.figure()
sns.histplot(data=df, x="phishing_score", hue="label", bins=10, multiple="dodge")
plt.title("Phishing Score Distribution (Normal vs Suspicious)")
plt.savefig("outputs/phishing_score_dist.png")
plt.close()

print("\nSaved plots to outputs/ folder.")
