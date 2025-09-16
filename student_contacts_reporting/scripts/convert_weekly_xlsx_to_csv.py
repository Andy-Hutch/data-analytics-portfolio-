import pandas as pd
from pathlib import Path

XLSX_PATH = Path("reports/weekly_summary.xlsx")
CSV_PATH = Path("reports/weekly_summary.csv")

df = pd.read_excel(XLSX_PATH, engine="openpyxl")
df.to_csv(CSV_PATH, index=False)
print("✅ Converted weekly_summary.xlsx to weekly_summary.csv")
