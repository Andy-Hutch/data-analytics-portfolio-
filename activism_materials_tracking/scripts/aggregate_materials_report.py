# Aggregate and visualize activism materials data
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

input_path = 'activism_materials_tracking/data/materials_log_clean.csv'
charts_dir = 'activism_materials_tracking/reports/charts/'
os.makedirs(charts_dir, exist_ok=True)

# Load data
df = pd.read_csv(input_path)

# Convert date to week
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Week'] = df['Date'].dt.strftime('%Y-%U')

# Clean Quantity
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0)

# Aggregate by chapter (Location)
by_chapter = df.groupby('Location')['Quantity'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
by_chapter.plot(kind='bar', color='skyblue')
plt.title('Total Materials by Chapter')
plt.ylabel('Total Quantity')
plt.xlabel('Chapter')
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, 'materials_by_chapter.png'))
plt.close()

# Aggregate by week
by_week = df.groupby('Week')['Quantity'].sum()
plt.figure(figsize=(10,5))
by_week.plot(kind='line', marker='o', color='green')
plt.title('Total Materials by Week')
plt.ylabel('Total Quantity')
plt.xlabel('Week')
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, 'materials_by_week.png'))
plt.close()

# Aggregate by material type
by_material = df.groupby('Material')['Quantity'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
by_material.plot(kind='bar', color='orange')
plt.title('Total Materials by Type')
plt.ylabel('Total Quantity')
plt.xlabel('Material Type')
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, 'materials_by_type.png'))
plt.close()

print('Charts saved to', charts_dir)