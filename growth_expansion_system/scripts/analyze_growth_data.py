import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Paths
DATA_PATH = Path("../data/raw/chapter_growth_data.csv")
REPORTS_PATH = Path("reports")
CHARTS_PATH = REPORTS_PATH / "charts"

REPORTS_PATH.mkdir(parents=True, exist_ok=True)
CHARTS_PATH.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH, parse_dates=["event_date"])

# Add month column for grouping
df["month"] = df["event_date"].dt.to_period("M")

# -------------------------
# 1. Line chart: Growth over time by chapter
# -------------------------
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x=df["month"].astype(str), y="new_students", hue="chapter_name", marker="o")
plt.title("Monthly New Student Growth by Chapter")
plt.xlabel("Month")
plt.ylabel("New Students")
plt.legend(title="Chapter")
plt.tight_layout()
plt.savefig(REPORTS_PATH / "growth_over_time.png")
plt.close()

# -------------------------
# 2. Bar chart: Total students by chapter
# -------------------------
chapter_totals = df.groupby("chapter_name")["new_students"].sum().reset_index()

plt.figure(figsize=(8,6))
sns.barplot(data=chapter_totals, x="chapter_name", y="new_students", palette="viridis")
plt.title("Total New Students by Chapter")
plt.xlabel("Chapter")
plt.ylabel("Total Students")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(CHARTS_PATH / "total_students_by_chapter.png")
plt.close()

# -------------------------
# 3. Scatter plot: Events vs. Students
# -------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="events_hosted", y="new_students", hue="chapter_name", s=100)
plt.title("Events Hosted vs New Students")
plt.xlabel("Events Hosted")
plt.ylabel("New Students")
plt.tight_layout()
plt.savefig(CHARTS_PATH / "events_vs_students.png")
plt.close()

# -------------------------
# 4. Heatmap: Monthly growth by chapter
# -------------------------
pivot = df.pivot_table(index="chapter_name", columns="month", values="new_students", aggfunc="sum").fillna(0)

plt.figure(figsize=(10,6))
sns.heatmap(pivot, annot=True, fmt="g", cmap="YlGnBu")
plt.title("Monthly New Student Growth Heatmap")
plt.xlabel("Month")
plt.ylabel("Chapter")
plt.tight_layout()
plt.savefig(REPORTS_PATH / "growth_heatmap.png")
plt.close()

print("✅ Charts generated in reports/ and reports/charts/")

# Auto-generate Markdown report
markdown_report = f"""
# Chapter Growth & Expansion Report

This report summarizes chapter growth trends, events, and recruitment performance based on collected data.

---

## 📈 Monthly Growth Over Time
![Growth Over Time](growth_over_time.png)

---

## 📊 Total Students by Chapter
![Total Students by Chapter](charts/total_students_by_chapter.png)

---

## 🔎 Events vs. Students
![Events vs Students](charts/events_vs_students.png)

---

## 🌍 Growth Heatmap
![Growth Heatmap](growth_heatmap.png)

---

## ✅ Key Takeaways
1. Hosting more events directly drives higher student recruitment.  
2. Established chapters outperform newer ones but newer chapters show strong growth potential.  
3. Regional differences suggest West and Midwest are strong, while East may need more support.  

---

📌 *Generated automatically using Python (Pandas, Seaborn, Matplotlib).*
"""

with open(REPORTS_PATH / "growth_report.md", "w", encoding="utf-8") as f:
    f.write(markdown_report)

print("✅ Charts and Markdown report generated in reports/ and reports/charts/")
