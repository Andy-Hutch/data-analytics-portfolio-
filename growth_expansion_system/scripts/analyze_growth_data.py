import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Robust path resolution for data file
script_dir = os.path.dirname(__file__)
data_path = os.path.abspath(os.path.join(script_dir, '..', 'data', 'growth_data_clean.csv'))
reports_dir = os.path.abspath(os.path.join(script_dir, '..', 'reports'))
charts_dir = os.path.abspath(os.path.join(reports_dir, 'charts'))

# Ensure output directories exist
os.makedirs(reports_dir, exist_ok=True)
os.makedirs(charts_dir, exist_ok=True)

# Load cleaned data
df = pd.read_csv(data_path)

# --- 1. Bar Chart: Total New Students by Chapter ---
chapter_summary = df.groupby('chapter')['new_students'].sum().reset_index()
plt.figure(figsize=(8, 6))
plt.bar(chapter_summary['chapter'], chapter_summary['new_students'], color='skyblue')
plt.title('Total New Students by Chapter')
plt.xlabel('Chapter')
plt.ylabel('Total New Students')
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, 'bar_total_students_by_chapter.png'))
plt.close()

# --- 2. Line Chart: Monthly Growth Trend ---
df['month'] = pd.to_datetime(df['date'], errors='coerce').dt.to_period('M')
monthly_growth = df.groupby('month')['new_students'].sum().reset_index()
plt.figure(figsize=(8, 6))
plt.plot(monthly_growth['month'].astype(str), monthly_growth['new_students'],
         marker='o', color='orange')
plt.title('Monthly New Student Growth')
plt.xlabel('Month')
plt.ylabel('New Students')
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, 'line_monthly_growth.png'))
plt.close()

# --- 3. Pie Chart: Student Distribution by Chapter ---
plt.figure(figsize=(6, 6))
plt.pie(chapter_summary['new_students'],
        labels=chapter_summary['chapter'],
        autopct='%1.1f%%',
        startangle=140)
plt.title('New Students Distribution by Chapter')
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'pie_students_distribution_by_chapter.png'))
plt.close()

# --- 4. Histogram: Distribution of New Students ---
plt.figure(figsize=(8, 6))
plt.hist(df['new_students'].dropna(), bins=10, color='green', edgecolor='black')
plt.title('Distribution of New Students per Event')
plt.xlabel('New Students')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'histogram_new_students.png'))
plt.close()

# --- 5. Scatter Plot: Active Events vs. New Students ---
plt.figure(figsize=(8, 6))
plt.scatter(df['active_events'], df['new_students'], color='purple')
plt.title('Active Events vs. New Students')
plt.xlabel('Active Events')
plt.ylabel('New Students')
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, 'scatter_events_vs_students.png'))
plt.close()

# --- 6. Heatmap: Monthly Growth by Chapter ---
heatmap_data = df.pivot_table(index='chapter', columns='month', values='new_students', aggfunc='sum')
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title('Monthly Growth Heatmap by Chapter')
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, 'heatmap_monthly_growth.png'))
plt.close()
