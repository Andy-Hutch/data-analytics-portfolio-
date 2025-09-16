import pandas as pd
import os

# Resolve paths relative to script location
script_dir = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(script_dir, '..', 'data'))
raw_path = os.path.join(data_dir, 'growth_data_raw.csv')
clean_path = os.path.join(data_dir, 'growth_data_clean.csv')

# Load raw data
df = pd.read_csv(raw_path)

# Standardize chapter names
df['chapter'] = df['chapter'].replace({'PHX': 'Phoenix'})

# Convert 'new_students' to numeric, coercing errors to NaN
df['new_students'] = pd.to_numeric(df['new_students'], errors='coerce')

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Standardize region names
df['region'] = df['region'].replace({'SW': 'Southwest'})

# Save cleaned data
df.to_csv(clean_path, index=False)
