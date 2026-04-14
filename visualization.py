import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load JSON file (update filename if needed)
file_path = "data/trends_20260414.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

print("Total records:", len(df))

# -----------------------------
# 1. Category Distribution
# -----------------------------
plt.figure(figsize=(8, 5))
category_counts = df["category"].value_counts()

plt.bar(category_counts.index, category_counts.values, color="skyblue")
plt.title("TrendPulse - Stories by Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# -----------------------------
# 2. Top 10 Authors
# -----------------------------
plt.figure(figsize=(8, 5))
top_authors = df["author"].value_counts().head(10)

plt.bar(top_authors.index, top_authors.values, color="orange")
plt.title("Top 10 Authors")
plt.xlabel("Author")
plt.ylabel("Number of Posts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Score Distribution
# -----------------------------
plt.figure(figsize=(8, 5))
plt.hist(df["score"], bins=20, color="green", edgecolor="black")
plt.title("Score Distribution of Stories")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Comments vs Score (Scatter)
# -----------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df["score"], df["num_comments"], alpha=0.6, color="red")
plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.tight_layout()
plt.show()