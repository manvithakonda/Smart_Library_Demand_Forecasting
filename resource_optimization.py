import pandas as pd

# ==========================================
# SMART LIBRARY RESOURCE OPTIMIZATION
# ==========================================

print("=" * 60)
print("SMART LIBRARY RESOURCE OPTIMIZATION")
print("=" * 60)

# Load forecast
forecast = pd.read_csv("library_demand_forecast.csv")

forecast["Month"] = pd.to_datetime(forecast["Month"])

# ==========================================
# 1. GENERATE RECOMMENDATIONS
# ==========================================

def recommendation(level):

    if level == "High Demand":
        return "Increase book availability, staff support and borrowing capacity"

    elif level == "Low Demand":
        return "Reduce excess stock and promote underused resources"

    else:
        return "Maintain normal inventory and staffing levels"


forecast["Recommendation"] = forecast["Demand_Level"].apply(
    recommendation
)

# ==========================================
# 2. DISPLAY RESULTS
# ==========================================

print("\n" + "=" * 60)
print("RESOURCE OPTIMIZATION RECOMMENDATIONS")
print("=" * 60)

print(
    forecast[
        ["Month", "Forecasted_Loans",
         "Demand_Level", "Recommendation"]
    ].to_string(index=False)
)

# ==========================================
# 3. SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("OPTIMIZATION SUMMARY")
print("=" * 60)

high = (forecast["Demand_Level"] == "High Demand").sum()
medium = (forecast["Demand_Level"] == "Medium Demand").sum()
low = (forecast["Demand_Level"] == "Low Demand").sum()

print("High-demand months:", high)
print("Medium-demand months:", medium)
print("Low-demand months:", low)

# ==========================================
# 4. SAVE RESULTS
# ==========================================

forecast.to_csv(
    "library_resource_optimization.csv",
    index=False
)

print("\nOutput file created:")
print("✓ library_resource_optimization.csv")

print("\n" + "=" * 60)
print("STEP 5 COMPLETED SUCCESSFULLY")
print("=" * 60)