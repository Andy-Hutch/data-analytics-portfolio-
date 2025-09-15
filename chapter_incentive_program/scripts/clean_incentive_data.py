import pandas as pd
import numpy as np

# Input and output file paths
input_file = 'data/incentive_data_raw.csv'
output_file = 'data/incentive_data_clean.csv'

# Read raw data
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"Input file not found: {input_file}")
    exit(1)

# Basic cleaning steps
# 1. Remove duplicates
initial_count = len(df)
df = df.drop_duplicates()
removed_duplicates = initial_count - len(df)

# 2. Remove rows with missing or invalid values
# (Assume incentive amount must be > 0 and date must be valid)
df = df.dropna(subset=['Chapter', 'Program', 'MemberID', 'IncentiveAmount', 'DateAwarded'])
df = df[df['IncentiveAmount'] > 0]

# 3. Standardize column names (strip whitespace)
df.columns = [col.strip() for col in df.columns]

# 4. Convert DateAwarded to datetime, drop rows with invalid dates
def is_valid_date(date_str):
    try:
        pd.to_datetime(date_str, format='%Y-%m-%d')
        return True
    except Exception:
        return False

df = df[df['DateAwarded'].apply(is_valid_date)]
df['DateAwarded'] = pd.to_datetime(df['DateAwarded'], format='%Y-%m-%d')

# Save cleaned data
try:
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
    print(f"Duplicates removed: {removed_duplicates}")
    print(f"Final record count: {len(df)}")
except Exception as e:
    print(f"Error saving cleaned data: {e}")
