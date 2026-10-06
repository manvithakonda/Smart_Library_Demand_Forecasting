import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

# ==========================================
# SMART LIBRARY DEMAND FORECASTING
# ==========================================

print("=" * 60)
print("SMART LIBRARY DEMAND FORECASTING")
print("=" * 60)

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("loans.csv")

df["Month"] = pd.to_datetime(df["Month"], format="%Y-%m")
df["Loans"] = pd.to_numeric(df["Loans"], errors="coerce")

df = df.dropna(subset=["Month", "Loans"])
df = df[df["Loans"] >= 0]

# ==========================================
# 2. CALCULATE MONTHLY DEMAND
# ==========================================

monthly_demand = (
    df.groupby("Month")["Loans"]
    .sum()
    .sort_index()
    .reset_index()
)

print("\nHistorical monthly demand:")
print(monthly_demand.tail(10))

# ==========================================
# 3. CREATE TIME INDEX
# ==========================================

monthly_demand["Time_Index"] = np.arange(len(monthly_demand))

X = monthly_demand[["Time_Index"]]
y = monthly_demand["Loans"]

# ==========================================
# 4. TRAIN FORECASTING MODEL
# ==========================================

model = LinearRegression()

model.fit(X, y)

# ==========================================
# 5. FORECAST NEXT 6 MONTHS
# ==========================================

future_indices = np.arange(
    len(monthly_demand),
    len(monthly_demand) + 6
).reshape(-1, 1)

forecast_values = model.predict(future_indices)

last_month = monthly_demand["Month"].max()

future_months = pd.date_range(
    start=last_month + pd.DateOffset(months=1),
    periods=6,
    freq="MS"
)

forecast = pd.DataFrame({
    "Month": future_months,
    "Forecasted_Loans": forecast_values
})

forecast["Forecasted_Loans"] = (
    forecast["Forecasted_Loans"]
    .clip(lower=0)
    .round()
    .astype(int)
)

# ==========================================
# 6. DISPLAY FORECAST
# ==========================================

print("\n" + "=" * 60)
print("NEXT 6 MONTHS DEMAND FORECAST")
print("=" * 60)

print(forecast.to_string(index=False))

# ==========================================
# 7. DEMAND CLASSIFICATION
# ==========================================

average_demand = monthly_demand["Loans"].mean()

high_threshold = average_demand * 1.20
low_threshold = average_demand * 0.80

def classify_demand(value):

    if value >= high_threshold:
        return "High Demand"

    elif value <= low_threshold:
        return "Low Demand"

    else:
        return "Medium Demand"


forecast["Demand_Level"] = forecast["Forecasted_Loans"].apply(
    classify_demand
)

print("\n" + "=" * 60)
print("FORECAST DEMAND LEVEL")
print("=" * 60)

print(forecast.to_string(index=False))

# ==========================================
# 8. SAVE FORECAST
# ==========================================

forecast.to_csv(
    "library_demand_forecast.csv",
    index=False
)

# ==========================================
# 9. FORECAST GRAPH
# ==========================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_demand["Month"],
    monthly_demand["Loans"],
    label="Historical Demand"
)

plt.plot(
    forecast["Month"],
    forecast["Forecasted_Loans"],
    marker="o",
    linestyle="--",
    label="Forecast"
)

plt.title("Library Loan Demand Forecast")
plt.xlabel("Month")
plt.ylabel("Number of Loans")

plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "library_demand_forecast.png",
    dpi=300
)

# ==========================================
# COMPLETION
# ==========================================

print("\n" + "=" * 60)
print("STEP 4 COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nFiles created:")
print("✓ library_demand_forecast.csv")
print("✓ library_demand_forecast.png")