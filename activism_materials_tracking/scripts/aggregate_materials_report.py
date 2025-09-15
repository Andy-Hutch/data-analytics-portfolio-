# Aggregate, analyze, and visualize activism materials data
import pandas as pd
import matplotlib.pyplot as plt
import os

input_path = 'activism_materials_tracking/data/materials_log_clean.csv'
charts_dir = 'activism_materials_tracking/reports/charts/'
reports_dir = 'activism_materials_tracking/reports/'
os.makedirs(charts_dir, exist_ok=True)
os.makedirs(reports_dir, exist_ok=True)

# Load data
df = pd.read_csv(input_path)

# Convert date to week
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Week'] = df['Date'].dt.strftime('%Y-%U')

# Clean Quantity
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0)

# Weekly inventory summary (pivot table)
weekly_summary = df.pivot_table(index='Week', columns='Material', values='Quantity', aggfunc='sum', fill_value=0)
weekly_summary.to_excel(os.path.join(reports_dir, 'weekly_inventory_summary.xlsx'))
weekly_summary.to_csv(os.path.join(reports_dir, 'weekly_inventory_summary.csv'))
# Aggregate, analyze, and visualize activism materials data
import pandas as pd
import matplotlib.pyplot as plt
import os

input_path = 'activism_materials_tracking/data/materials_log_clean.csv'
charts_dir = 'activism_materials_tracking/reports/charts/'
reports_dir = 'activism_materials_tracking/reports/'
os.makedirs(charts_dir, exist_ok=True)
os.makedirs(reports_dir, exist_ok=True)

# Load data
df = pd.read_csv(input_path)

# Convert date to week
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Week'] = df['Date'].dt.strftime('%Y-%U')

# Clean Quantity
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0)

# Aggregate by chapter (Location)
by_chapter = df.groupby('Location')['Quantity'].sum().sort_values(ascending=False)
by_chapter.to_csv(os.path.join(reports_dir, 'materials_by_chapter.csv'))
by_chapter.to_excel(os.path.join(reports_dir, 'materials_by_chapter.xlsx'))

# Also save as CSV for GitHub readability
by_chapter.to_csv(os.path.join(reports_dir, 'materials_by_chapter.csv'))
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
by_week.to_csv(os.path.join(reports_dir, 'materials_by_week.csv'))
by_week.to_excel(os.path.join(reports_dir, 'materials_by_week.xlsx'))

# Also save as CSV for GitHub readability
by_week.to_csv(os.path.join(reports_dir, 'materials_by_week.csv'))
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
by_material.to_csv(os.path.join(reports_dir, 'materials_by_type.csv'))
by_material.to_excel(os.path.join(reports_dir, 'materials_by_type.xlsx'))

# Also save as CSV for GitHub readability
by_material.to_csv(os.path.join(reports_dir, 'materials_by_type.csv'))
plt.figure(figsize=(8,5))
by_material.plot(kind='bar', color='orange')
plt.title('Total Materials by Type')
plt.ylabel('Total Quantity')
plt.xlabel('Material Type')
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, 'materials_by_type.png'))
plt.close()

# Weekly inventory summary (pivot table)
weekly_summary = df.pivot_table(index='Week', columns='Material', values='Quantity', aggfunc='sum', fill_value=0)
weekly_summary.to_excel(os.path.join(reports_dir, 'weekly_inventory_summary.xlsx'))


# Weekly inventory summary (pivot table)
weekly_summary = df.pivot_table(index='Week', columns='Material', values='Quantity', aggfunc='sum', fill_value=0)
weekly_summary.to_excel(os.path.join(reports_dir, 'weekly_inventory_summary.xlsx'))

print('Charts and summary files saved to', charts_dir, 'and', reports_dir)
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