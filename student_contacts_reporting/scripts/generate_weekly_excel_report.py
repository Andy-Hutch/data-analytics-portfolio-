import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/contacts_clean.csv")
REPORT_PATH = Path("reports/weekly_summary.xlsx")

df = pd.read_csv(DATA_PATH, parse_dates=["created_date"])

df["week"] = df["created_date"].dt.to_period("W")
weekly_counts = df.groupby("week").size().reset_index(name="contacts")
weekly_counts["week"] = weekly_counts["week"].astype(str)

weekly_counts.to_excel(REPORT_PATH, index=False, engine="openpyxl")
print("✅ Weekly summary Excel report generated in reports/weekly_summary.xlsx")
