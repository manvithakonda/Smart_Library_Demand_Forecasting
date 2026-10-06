import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# SMART LIBRARY DEMAND ANALYZER
# VISUAL ANALYSIS
# ==========================================

df = pd.read_csv("loans.csv")

# Convert columns
df["Month"] = pd.to_datetime(df["Month"], format="%Y-%m")
df["Loans"] = pd.to_numeric(df["Loans"], errors="coerce")

# Clean data
df = df.dropna(subset=["Library name", "Month", "Type", "Loans"])
df = df.drop_duplicates()
df = df[df["Loans"] >= 0]

# ==========================================
# CHART 1: TOP 10 LIBRARIES
# ==========================================

library_demand = (
    df.groupby("Library name")["Loans"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
library_demand.plot(kind="barh")

plt.title("Top 10 Libraries by Total Loan Demand")
plt.xlabel("Total Loans")
plt.ylabel("Library")

plt.tight_layout()
plt.savefig("top_10_libraries.png", dpi=300)
plt.show()

# ==========================================
# CHART 2: RESOURCE TYPE DEMAND
# ==========================================

type_demand = (
    df.groupby("Type")["Loans"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
type_demand.plot(kind="bar")

plt.title("Library Demand by Resource Type")
plt.xlabel("Resource Type")
plt.ylabel("Total Loans")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("resource_type_demand.png", dpi=300)
plt.show()

# ==========================================
# CHART 3: MONTHLY DEMAND TREND
# ==========================================

monthly_demand = (
    df.groupby("Month")["Loans"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_demand.index,
    monthly_demand.values,
    marker="o"
)

plt.title("Monthly Library Loan Demand Trend")
plt.xlabel("Month")
plt.ylabel("Total Loans")

plt.xticks(rotation=45)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("monthly_demand_trend.png", dpi=300)
plt.show()

# ==========================================
# CHART 4: MONTHLY DEMAND HEATMAP
# ==========================================

heatmap_data = df.copy()

heatmap_data["Year"] = heatmap_data["Month"].dt.year
heatmap_data["Month_Number"] = heatmap_data["Month"].dt.month

monthly_year = (
    heatmap_data
    .groupby(["Year", "Month_Number"])["Loans"]
    .sum()
    .unstack()
)

plt.figure(figsize=(12, 6))

sns.heatmap(
    monthly_year,
    annot=True,
    fmt=".0f"
)

plt.title("Library Demand Heatmap by Year and Month")
plt.xlabel("Month")
plt.ylabel("Year")

plt.tight_layout()
plt.savefig("demand_heatmap.png", dpi=300)
plt.show()

# ==========================================
# COMPLETION
# ==========================================

print("\n" + "=" * 60)
print("STEP 3 COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nCharts created:")
print("✓ top_10_libraries.png")
print("✓ resource_type_demand.png")
print("✓ monthly_demand_trend.png")
print("✓ demand_heatmap.png")