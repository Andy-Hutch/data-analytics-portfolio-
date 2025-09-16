📊 Growth & Expansion System

This project simulates a real-world data analytics workflow for tracking and analyzing chapter growth across student organizations. It includes raw and cleaned data, automated analysis scripts, visualizations, and a polished PDF report—mirroring what a data analyst might deliver to stakeholders.

# 📂 Project Structure

```
growth_expansion_system/
│── data/
│   ├── raw/                      # Placeholder for raw input files
│   ├── processed/                # Cleaned and transformed datasets
│
│── reports/
│   ├── chapter_growth_report.pdf # Final report (auto-generated)
│   ├── student_growth_over_time.png
│   ├── chapter_distribution.png
│   └── charts/
│       ├── events_vs_students.png
│       ├── students_distribution.png
│       └── monthly_growth_heatmap.png
│
│── scripts/
│   ├── analyze_growth_data.py    # Generates charts from data
│   └── generate_report.py        # Builds PDF report with charts + analysis
│
└── README.md                     # Project documentation
```

# ⚙️ Workflow

## Data Collection

Example student recruitment & chapter activity data is stored in `data/`.

This simulates real-world student organization growth tracking.

## Analysis & Visualization

Run `scripts/analyze_growth_data.py` to generate charts:

```powershell
python scripts/analyze_growth_data.py
```

## Report Generation

Compile insights + charts into a stakeholder-ready PDF:

```powershell
python scripts/generate_report.py
```

# Output

- PDF report (`reports/chapter_growth_report.pdf`)
- PNG charts (`reports/` + `reports/charts/`)

# 📈 Example Insights

- Student recruitment trends over time
- Chapter distribution by size
- Correlation between events and new students
- Monthly growth patterns (heatmap view)

# 🎯 Real-World Application

This project mirrors deliverables an analyst might provide to an organization like TPUSA or other student/nonprofit groups:

- Track growth over time
- Identify high-performing chapters
- Recommend resource allocation & outreach strategies

# 🛠️ Tools & Libraries

- Python (`pandas`, `matplotlib`, `seaborn`) – data analysis + visualization
- ReportLab – PDF report generation
- GitHub – version control & portfolio showcase

# 🔧 How to run

Save the dataset to:
growth_expansion_system/data/raw/chapter_growth_data.csv

Save the script to:
growth_expansion_system/scripts/analyze_growth_data.py

In VS Code terminal:

```powershell
cd growth_expansion_system/scripts
python analyze_growth_data.py
```

Check growth_expansion_system/reports/ and growth_expansion_system/reports/charts/ → you’ll have 4 polished PNGs.
