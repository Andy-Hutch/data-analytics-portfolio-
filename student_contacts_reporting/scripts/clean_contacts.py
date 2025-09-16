import pandas as pd
from pathlib import Path

RAW_PATH = Path("../data/contacts_raw.csv")
PROCESSED_PATH = Path("../data/contacts_clean.csv")

# Load data
df = pd.read_csv(RAW_PATH, parse_dates=["created_date"])

# Standardize email (lowercase, strip spaces)
df["email"] = df["email"].str.lower().str.strip()

# Drop duplicates by email
df = df.drop_duplicates(subset="email")

# Standardize school names (title case)
df["school"] = df["school"].str.title()

# Save cleaned data
PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(PROCESSED_PATH, index=False)

print("✅ Cleaned student contacts saved to processed/")

