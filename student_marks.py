import pandas as pd
import matplotlib.pyplot as plt

# Input Data
data = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

# (a) Clean Name
df["Name"] = df["Name"].str.strip().str.title()

# (b) Convert Marks and fill "absent" with mean
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(round(mean_marks, 2))

# (c) Print cleaned DataFrame
print("--- Cleaned Student Marks DataFrame ---")
print(df)

# (d) Draw Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"], color="skyblue", edgecolor="black")
plt.title("Student Marks Distribution")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.savefig("marks_bar.png")
plt.show()
