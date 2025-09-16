import pandas as pd
from pathlib import Path
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

DATA_PATH = Path("data/contacts_clean.csv")
REPORT_PATH = Path("reports/monthly_summary.pdf")

df = pd.read_csv(DATA_PATH, parse_dates=["created_date"])

# Monthly aggregation
df["month"] = df["created_date"].dt.to_period("M")
monthly_counts = df.groupby("month").size().reset_index(name="contacts")

with PdfPages(REPORT_PATH) as pdf:
    # Page 1: Monthly contacts line chart
    plt.figure(figsize=(8,5))
    plt.plot(monthly_counts["month"].astype(str), monthly_counts["contacts"], marker="o")
    plt.title("Monthly New Student Contacts")
    plt.xlabel("Month")
    plt.ylabel("Contacts")
    plt.xticks(rotation=45)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # Page 2: Contacts by State bar chart
    state_counts = df["state"].value_counts().reset_index()
    state_counts.columns = ["state", "contacts"]
    plt.figure(figsize=(8,5))
    plt.bar(state_counts["state"], state_counts["contacts"], color="skyblue")
    plt.title("Contacts by State")
    plt.xlabel("State")
    plt.ylabel("Contacts")
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # Page 3: Contacts by Source pie chart
    source_counts = df["source"].value_counts().reset_index()
    source_counts.columns = ["source", "contacts"]
    plt.figure(figsize=(6,6))
    plt.pie(source_counts["contacts"], labels=source_counts["source"], autopct="%1.1f%%", startangle=140)
    plt.title("Contacts by Source")
    plt.tight_layout()
    pdf.savefig()
    plt.close()

print("✅ Monthly PDF report generated in reports/monthly_summary.pdf")
