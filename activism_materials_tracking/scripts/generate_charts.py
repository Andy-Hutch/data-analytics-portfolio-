import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
# Update the filename if needed (e.g., materials_log_clean.csv)
data_path = "data/materials_log_clean.csv"
charts_path = "reports/charts/"

# Ensure charts folder exists
os.makedirs(charts_path, exist_ok=True)

df = pd.read_csv(data_path)

# Example 1: Materials by Week
if "Week" in df.columns and "Quantity" in df.columns:
    materials_by_week = df.groupby("Week")["Quantity"].sum()
    materials_by_week.plot(kind="bar", figsize=(8, 5), title="Materials Distributed by Week")
    plt.ylabel("Quantity")
    plt.tight_layout()
    plt.savefig(os.path.join(charts_path, "materials_by_week.png"))
    plt.close()

# Example 2: Materials by Type
if "Material_Type" in df.columns and "Quantity" in df.columns:
    materials_by_type = df.groupby("Material_Type")["Quantity"].sum()
    materials_by_type.plot(kind="pie", figsize=(6, 6), autopct='%1.1f%%', title="Materials by Type")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(charts_path, "materials_by_type.png"))
    plt.close()

# Example 3: Materials by Chapter
if "Chapter" in df.columns and "Quantity" in df.columns:
    materials_by_chapter = df.groupby("Chapter")["Quantity"].sum()
    materials_by_chapter.plot(kind="bar", figsize=(8, 5), title="Materials Distributed by Chapter")
    plt.ylabel("Quantity")
    plt.tight_layout()
    plt.savefig(os.path.join(charts_path, "materials_by_chapter.png"))
    plt.close()

print("✅ Charts generated and saved in 'reports/charts/' folder.")
