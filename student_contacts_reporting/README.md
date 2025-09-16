# Student Contacts Reporting System

This project simulates a **real-world data analytics workflow** for tracking and reporting student contact data across multiple schools and regions. It includes raw and cleaned datasets, automated data cleaning, weekly visualizations, and a Markdown report—mirroring professional analytics deliverables.

---



## 📂 Project Structure

student_contacts_reporting/
│
├── data/
│   ├── contacts_raw.csv         # Incoming student contact data (CSV)
│   └── contacts_clean.csv       # Cleaned & standardized data
│
├── scripts/
│   ├── clean_contacts.py                # Cleans and validates raw data
│   ├── weekly_report.py                 # Generates weekly summary report, dashboard, and charts
│   ├── generate_monthly_pdf_report.py   # Creates monthly PDF report
│   ├── generate_weekly_excel_report.py  # Creates weekly Excel report
│   └── convert_weekly_xlsx_to_csv.py    # Converts weekly Excel report to CSV
│
├── reports/
│   ├── contacts_summary.md      # Weekly Markdown report (auto-generated)
│   ├── contacts_dashboard.md    # Dashboard-style Markdown report
│   ├── monthly_summary.pdf      # Monthly PDF report
│   ├── weekly_summary.xlsx      # Weekly Excel report
│   ├── weekly_summary.csv       # Weekly CSV report (converted from Excel)
│   └── charts/
│       ├── weekly_contacts.png        # Weekly contacts growth chart
│       ├── contacts_by_state.png      # Contacts by state chart
│       └── contacts_by_source.png     # Contacts by source chart
│
└── README.md # Project documentation

---

## ⚙️ Workflow


1. **Data Collection**  
   - Raw student contacts (name, email, school, state, source, date) are stored in `data/contacts_raw.csv`.

2. **Data Cleaning**  
   - Run `scripts/clean_contacts.py` to:
     - Standardize emails and school names  
     - Remove duplicates  
     - Save cleaned dataset to `data/contacts_clean.csv`

3. **Weekly Reporting & Dashboard**  
   - Run `scripts/weekly_report.py` to:
     - Generate visualizations (weekly contacts growth, contacts by state, contacts by source)  
     - Auto-generate `contacts_summary.md` and `contacts_dashboard.md` in `reports/`  
     - Save charts in `reports/charts/`

4. **Monthly PDF Report**  
   - Run `scripts/generate_monthly_pdf_report.py` to:
     - Create a multi-page PDF report with monthly trends, state breakdown, and source analysis
     - Output: `reports/monthly_summary.pdf`

5. **Weekly Excel & CSV Reports**  
   - Run `scripts/generate_weekly_excel_report.py` to:
     - Generate a weekly summary in Excel format (`reports/weekly_summary.xlsx`)
   - Run `scripts/convert_weekly_xlsx_to_csv.py` to:
     - Convert the Excel report to CSV (`reports/weekly_summary.csv`)

6. **Output Summary**  
   - Markdown reports: `contacts_summary.md`, `contacts_dashboard.md`  
   - PDF report: `monthly_summary.pdf`  
   - Excel report: `weekly_summary.xlsx`  
   - CSV report: `weekly_summary.csv`  
   - PNG charts: `charts/`  

---

## 📊 Example Visualizations & Reports
- **Weekly New Student Contacts** – line chart showing growth over time  
- **Contacts by State** – bar chart showing geographic distribution  
- **Contacts by Source** – pie chart showing channel breakdown  
- **Weekly Markdown Report** – summary and insights for each week  
- **Dashboard Markdown Report** – portfolio-ready dashboard for leadership  
- **Monthly PDF Report** – multi-page PDF for professional presentation  
- **Weekly Excel/CSV Reports** – tabular summaries for further analysis  

---

## 🛠️ Tools & Libraries
- **Python** (Pandas, Seaborn, Matplotlib, openpyxl) – for data cleaning, analysis, visualization, and Excel/CSV conversion  
- **GitHub** – version control & portfolio showcase  

---

## 🎯 Real-World Application
This project simulates analytics work in a high-volume student organization setting:
- Track student recruitment trends  
- Identify strong vs. underperforming regions  
- Analyze recruitment channels and optimize outreach  
- Provide weekly/monthly reports for leadership or national teams  

---

📌 *This project is a portfolio simulation, designed to demonstrate data analytics skills, automated reporting, and real-world deliverables for professional settings.*

