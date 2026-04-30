import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================
# 📥 LOAD DATA
# ================================
df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\ecommerce-analytics-project\data\processed\final_dataset.csv")

# ================================
# 🔍 BASIC CHECKS
# ================================
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# ================================
# 📊 TOP 10 CATEGORIES BY REVENUE
# ================================
top = df.sort_values("revenue", ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top, x="revenue", y="category")
plt.title("Top 10 Revenue Generating Categories")
plt.xlabel("Revenue")
plt.ylabel("Category")

plt.savefig(r"C:\Users\HP\OneDrive\Documents\ecommerce-analytics-project\outputs\charts\top_10_categories.png", bbox_inches='tight')
plt.show()

# ================================
# 📊 REVENUE DISTRIBUTION
# ================================
plt.figure(figsize=(8,5))
sns.histplot(df["revenue"], kde=True)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Count")

plt.savefig(r"C:\Users\HP\OneDrive\Documents\ecommerce-analytics-project\outputs\charts\revenue_distribution.png", bbox_inches='tight')
plt.show()

# ================================
# 📊 BOXPLOT (OUTLIERS)
# ================================
plt.figure(figsize=(8,5))
sns.boxplot(x=df["revenue"])
plt.title("Revenue Distribution (Boxplot)")
plt.xlabel("Revenue")

plt.savefig(r"C:\Users\HP\OneDrive\Documents\ecommerce-analytics-project\outputs\charts\revenue_boxplot.png", bbox_inches='tight')
plt.show()

# ================================
# 📊 LOG TRANSFORMATION (ONLY FOR ANALYSIS)
# ================================
df["log_revenue"] = np.log1p(df["revenue"])

plt.figure(figsize=(8,5))
sns.histplot(df["log_revenue"], kde=True)
plt.title("Log Transformed Revenue (Analysis Only)")
plt.xlabel("Log Revenue")
plt.ylabel("Count")

plt.savefig(r"C:\Users\HP\OneDrive\Documents\ecommerce-analytics-project\outputs\charts\log_revenue.png", bbox_inches='tight')
plt.show()