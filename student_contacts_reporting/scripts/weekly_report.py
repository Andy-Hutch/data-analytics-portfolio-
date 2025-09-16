import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA_PATH = Path("../data/contacts_clean.csv")
REPORTS_PATH = Path("../reports")
CHARTS_PATH = REPORTS_PATH / "charts"

REPORTS_PATH.mkdir(parents=True, exist_ok=True)
CHARTS_PATH.mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_csv(DATA_PATH, parse_dates=["created_date"])

# Weekly aggregation
df["week"] = df["created_date"].dt.to_period("W")
weekly_counts = df.groupby("week").size().reset_index(name="contacts")
weekly_counts["week"] = weekly_counts["week"].astype(str)  # Convert to string for plotting

# Chart: Contacts per week
plt.figure(figsize=(8,5))
sns.lineplot(data=weekly_counts, x="week", y="contacts", marker="o")
plt.title("Weekly New Student Contacts")
plt.xlabel("Week")
plt.ylabel("Contacts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHARTS_PATH / "weekly_contacts.png")
plt.close()

# Chart: Contacts by State
state_counts = df["state"].value_counts().reset_index()
state_counts.columns = ["state", "contacts"]

plt.figure(figsize=(8,5))
sns.barplot(data=state_counts, x="state", y="contacts", palette="coolwarm")
plt.title("Contacts by State")
plt.xlabel("State")
plt.ylabel("Contacts")
plt.tight_layout()
plt.savefig(CHARTS_PATH / "contacts_by_state.png")
plt.close()

# Chart: Contacts by Source
source_counts = df["source"].value_counts().reset_index()
source_counts.columns = ["source", "contacts"]

plt.figure(figsize=(6,6))
plt.pie(source_counts["contacts"], labels=source_counts["source"], autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
plt.title("Contacts by Source")
plt.tight_layout()
plt.savefig(CHARTS_PATH / "contacts_by_source.png")
plt.close()

# Auto-generate Weekly Markdown report
markdown_report = f"""
# Student Contacts Weekly Report

---

## 📈 Weekly Growth
![Weekly Contacts](charts/weekly_contacts.png)

**Insight:** Student contacts are growing steadily week by week.

---

## 🌍 Contacts by State
![Contacts by State](charts/contacts_by_state.png)

**Insight:** Recruitment is strongest in Texas and Arizona, with California and Florida emerging.

---

## 📊 Contacts by Source
![Contacts by Source](charts/contacts_by_source.png)

**Insight:** Event Signups contribute the most contacts, followed by Website Forms and Referrals.

---

📌 *Generated automatically using Python (Pandas, Seaborn, Matplotlib).*
"""

with open(REPORTS_PATH / "contacts_summary.md", "w", encoding="utf-8") as f:
    f.write(markdown_report)

print("✅ Weekly report and charts (including source analysis) generated in reports/")

# Auto-generate Dashboard Markdown
dashboard_report = f"""
# Student Contacts Dashboard

This dashboard summarizes student contact analytics for the High School Department.

---

## 1️⃣ Weekly Growth
![Weekly Contacts](charts/weekly_contacts.png)

**Insight:** Student contacts are growing steadily week by week. Peaks often follow major events or outreach campaigns.

---

## 2️⃣ Contacts by State
![Contacts by State](charts/contacts_by_state.png)

**Insight:** Recruitment is strongest in Texas and Arizona, with California and Florida showing emerging trends. Regional differences may guide targeted outreach.

---

## 3️⃣ Contacts by Source
![Contacts by Source](charts/contacts_by_source.png)

**Insight:** Event Signups contribute the largest portion of contacts, followed by Website Forms and Referrals. Optimizing the most effective channels can improve recruitment.

---

## 📌 Key Takeaways
- Hosting more events drives measurable increases in student contacts.  
- Focus on high-performing states for maximum impact.  
- Source analysis helps allocate resources effectively between events, website, and referrals.

---

*Generated automatically using Python (Pandas, Seaborn, Matplotlib) — ready for portfolio showcase.*
"""

with open(REPORTS_PATH / "contacts_dashboard.md", "w", encoding="utf-8") as f:
    f.write(dashboard_report)

print("✅ Dashboard Markdown report generated in reports/contacts_dashboard.md")
dashboard_report = f"""
# Student Contacts Dashboard

This dashboard summarizes student contact analytics for the High School Department.

---

## 1️⃣ Weekly Growth
![Weekly Contacts](charts/weekly_contacts.png)

**Insight:** Student contacts are growing steadily week by week. Peaks often follow major events or outreach campaigns.

---

## 2️⃣ Contacts by State
![Contacts by State](charts/contacts_by_state.png)

**Insight:** Recruitment is strongest in Texas and Arizona, with California and Florida showing emerging trends. Regional differences may guide targeted outreach.

---

## 3️⃣ Contacts by Source
![Contacts by Source](charts/contacts_by_source.png)

**Insight:** Event Signups contribute the largest portion of contacts, followed by Website Forms and Referrals. Optimizing the most effective channels can improve recruitment.

---

## 📌 Key Takeaways
- Hosting more events drives measurable increases in student contacts.  
- Focus on high-performing states for maximum impact.  
- Source analysis helps allocate resources effectively between events, website, and referrals.

---

*Generated automatically using Python (Pandas, Seaborn, Matplotlib) — ready for portfolio showcase.*
"""

with open(REPORTS_PATH / "contacts_dashboard.md", "w", encoding="utf-8") as f:
    f.write(dashboard_report)

print("✅ Dashboard Markdown report generated in reports/contacts_dashboard.md")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA_PATH = Path("../data/contacts_clean.csv")
REPORTS_PATH = Path("../reports")
CHARTS_PATH = REPORTS_PATH / "charts"

REPORTS_PATH.mkdir(parents=True, exist_ok=True)
CHARTS_PATH.mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_csv(DATA_PATH, parse_dates=["created_date"])

# Weekly aggregation
df["week"] = df["created_date"].dt.to_period("W")
weekly_counts = df.groupby("week").size().reset_index(name="contacts")
weekly_counts["week"] = weekly_counts["week"].astype(str)  # Convert to string for plotting

# Chart: Contacts per week
plt.figure(figsize=(8,5))
sns.lineplot(data=weekly_counts, x="week", y="contacts", marker="o")
plt.title("Weekly New Student Contacts")
plt.xlabel("Week")
plt.ylabel("Contacts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHARTS_PATH / "weekly_contacts.png")
plt.close()

# Chart: Contacts by State
state_counts = df["state"].value_counts().reset_index()
state_counts.columns = ["state", "contacts"]

plt.figure(figsize=(8,5))
sns.barplot(data=state_counts, x="state", y="contacts", palette="coolwarm")
plt.title("Contacts by State")
plt.xlabel("State")
plt.ylabel("Contacts")
plt.tight_layout()
plt.savefig(CHARTS_PATH / "contacts_by_state.png")
plt.close()

# Chart: Contacts by Source
source_counts = df["source"].value_counts().reset_index()
source_counts.columns = ["source", "contacts"]

plt.figure(figsize=(6,6))
plt.pie(source_counts["contacts"], labels=source_counts["source"], autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
plt.title("Contacts by Source")
plt.tight_layout()
plt.savefig(CHARTS_PATH / "contacts_by_source.png")
plt.close()

# Auto-generate Weekly Markdown report
markdown_report = f"""
# Student Contacts Weekly Report

---

## 📈 Weekly Growth
![Weekly Contacts](charts/weekly_contacts.png)

**Insight:** Student contacts are growing steadily week by week.

---

## 🌍 Contacts by State
![Contacts by State](charts/contacts_by_state.png)

**Insight:** Recruitment is strongest in Texas and Arizona, with California and Florida emerging.

---

## 📊 Contacts by Source
![Contacts by Source](charts/contacts_by_source.png)

**Insight:** Event Signups contribute the most contacts, followed by Website Forms and Referrals.

---

📌 *Generated automatically using Python (Pandas, Seaborn, Matplotlib).*
"""

with open(REPORTS_PATH / "contacts_summary.md", "w", encoding="utf-8") as f:
    f.write(markdown_report)

print("✅ Weekly report and charts (including source analysis) generated in reports/")

# Auto-generate Dashboard Markdown
dashboard_report = f"""
# Student Contacts Dashboard

This dashboard summarizes student contact analytics for the High School Department.

---

## 1️⃣ Weekly Growth
![Weekly Contacts](charts/weekly_contacts.png)

**Insight:** Student contacts are growing steadily week by week. Peaks often follow major events or outreach campaigns.

---

## 2️⃣ Contacts by State
![Contacts by State](charts/contacts_by_state.png)

**Insight:** Recruitment is strongest in Texas and Arizona, with California and Florida showing emerging trends. Regional differences may guide targeted outreach.

---

## 3️⃣ Contacts by Source
![Contacts by Source](charts/contacts_by_source.png)

**Insight:** Event Signups contribute the largest portion of contacts, followed by Website Forms and Referrals. Optimizing the most effective channels can improve recruitment.

---

## 📌 Key Takeaways
- Hosting more events drives measurable increases in student contacts.  
- Focus on high-performing states for maximum impact.  
- Source analysis helps allocate resources effectively between events, website, and referrals.

---

*Generated automatically using Python (Pandas, Seaborn, Matplotlib) — ready for portfolio showcase.*
"""

with open(REPORTS_PATH / "contacts_dashboard.md", "w", encoding="utf-8") as f:
    f.write(dashboard_report)

print("✅ Dashboard Markdown report generated in reports/contacts_dashboard.md")
state_counts.columns = ["state", "contacts"]

plt.figure(figsize=(8,5))
sns.barplot(data=state_counts, x="state", y="contacts", palette="coolwarm")
plt.title("Contacts by State")
plt.xlabel("State")
plt.ylabel("Contacts")
plt.tight_layout()
plt.savefig(CHARTS_PATH / "contacts_by_state.png")
plt.close()

# Auto-generate Markdown report
markdown_report = f"""
# Student Contacts Weekly Report

---

## 📈 Weekly Growth
![Weekly Contacts](charts/weekly_contacts.png)

**Insight:** Student contacts are growing steadily week by week.

---

## 🌍 Contacts by State
![Contacts by State](charts/contacts_by_state.png)

**Insight:** Recruitment is strongest in Texas and Arizona, with California and Florida emerging.

---

📌 *Generated automatically using Python (Pandas, Seaborn, Matplotlib).*
"""

with open(REPORTS_PATH / "contacts_summary.md", "w", encoding="utf-8") as f:
    f.write(markdown_report)

print("✅ Weekly report and charts generated in reports/")
