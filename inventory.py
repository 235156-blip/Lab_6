import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt

# Dataset from manual
data = {
    "Product": ["Cola", "Chips", "Milk", "Juice", "Biscuits", "Cheese", "Water", "Nuts", "Yogurt", "Soda"],
    "Category": ["beverages ", "SNACKS", " Dairy", "beverages", "Snacks", "Dairy ", "BEVERAGES", " snacks", "DAIRY", "beverages"],
    "Price": ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 150", "Rs. 600", "Rs. 50", "Rs. 350", "Rs. 200", "Rs. 100"],
    "Stock": [40, 120, 60, 85, 110, 45, 150, 75, 50, 95]
}

df = pd.DataFrame(data)

# (a) Clean Category text
df["Category"] = df["Category"].str.strip().str.title()

# (b) Convert Price to numeric by removing "Rs. " and commas
df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False).str.replace(",", "").astype(float)

# (c) Label Encode Category
df["Category_Code"] = df["Category"].astype("category").cat.codes

print("--- Cleaned & Encoded Inventory DataFrame ---")
print(df)

# (d) Subplots: Bar Plot and Pie Chart side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Average Price per Category
avg_price = df.groupby("Category")["Price"].mean()
ax1.bar(avg_price.index, avg_price.values, color=["#4C78A8", "#F58518", "#54A24B"])
ax1.set_title("Average Price by Category")
ax1.set_xlabel("Category")
ax1.set_ylabel("Average Price (Rs.)")

# Plot 2: Stock Share by Category
total_stock = df.groupby("Category")["Stock"].sum()
ax2.pie(total_stock.values, labels=total_stock.index, autopct="%1.1f%%", startangle=90, colors=["#4C78A8", "#F58518", "#54A24B"])
ax2.set_title("Stock Share by Category")

plt.tight_layout()
plt.savefig("inventory_plots.png")
print("Saved inventory_plots.png successfully.")
