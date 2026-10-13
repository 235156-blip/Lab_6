import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset from manual (15 days, messy entries, missing humidity, 1 duplicate)
data = {
    "Date": ["2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05", 
             "2026-03-06", "2026-03-07", "2026-03-08", "2026-03-09", "2026-03-10",
             "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-01"],
    "City": [" Islamabad ", "ISLAMABAD", "islamabad", "Islamabad", " ISLAMABAD ",
             "Islamabad", "Islamabad", "islamabad ", "Islamabad", "ISLAMABAD",
             "Islamabad", "islamabad", "Islamabad", "ISLAMABAD", "Islamabad", " Islamabad "],
    "Temperature": ["32C", "28C", "25C", "30C", "34C", "22C", "24C", "31C", "33C", "29C", "27C", "23C", "35C", "26C", "30C", "32C"],
    "Humidity": [45, 60, np.nan, 50, 40, 75, np.nan, 48, 42, 55, np.nan, 70, 38, 62, 52, 45],
    "Condition": ["sunny", " Rainy", "CLOUDY ", "sunny ", "Sunny", "rainy", "Cloudy", "sunny", "SUNNY", "cloudy", "Rainy", "Cloudy", "sunny", "cloudy", "sunny", "sunny"]
}

df = pd.DataFrame(data)

# (a) Data Cleaning & Wrangling
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
df["Temperature"] = df["Temperature"].str.replace("C", "").astype(float)
df["Date"] = pd.to_datetime(df["Date"])

# Drop duplicate row
df = df.drop_duplicates()
print("Rows after dropping duplicates:", len(df))

# Fill missing humidity with median
median_humidity = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(median_humidity)
print("Missing Humidity filled with median:", median_humidity)

# (b) One-Hot Encoding for Condition
df_encoded = pd.get_dummies(df, columns=["Condition"], dtype=int)
print("\n--- Encoded Condition Columns ---")
print(df_encoded.filter(like="Condition_").head())

# Correlation
corr = df["Temperature"].corr(df["Humidity"])
print(f"\nCorrelation (Temperature, Humidity): {corr:.2f}")

# (c - f) 2x2 Subplot Dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Line Plot: Temperature over Date
axes[0, 0].plot(df["Date"].dt.strftime('%m-%d'), df["Temperature"], marker="o", color="crimson")
axes[0, 0].set_title("Temperature Trend Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (°C)")
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(True, alpha=0.3)

# 2. Scatter Plot: Temperature vs Humidity
axes[0, 1].scatter(df["Temperature"], df["Humidity"], color="purple", s=60)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (°C)")
axes[0, 1].set_ylabel("Humidity (%)")
axes[0, 1].grid(True, alpha=0.3)

# 3. Pie Chart: Condition distribution
condition_counts = df["Condition"].value_counts()
axes[1, 0].pie(condition_counts.values, labels=condition_counts.index, autopct="%1.1f%%", startangle=90)
axes[1, 0].set_title("Weather Condition Share")

# 4. Histogram: Temperature distribution
axes[1, 1].hist(df["Temperature"], bins=5, color="teal", edgecolor="white")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (°C)")
axes[1, 1].set_ylabel("Frequency")

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
print("Saved weather_dashboard.png successfully.")

# Show image window on screen
plt.show()
