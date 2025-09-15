# Activism Materials Tracking

## Overview
Tracks inventory and distribution of activism materials across chapters. Helps ensure transparency, accountability, and timely restocking. Key operations: logging materials, counting totals, generating weekly summary reports.

## Motivation
One of the tasks for the Club America Administrator is to log & track activism materials numerically. This repo simulates that workflow with sample data, cleaning, aggregation, and reporting.

## Workflow
1. Load raw data (`data/materials_log_raw.csv`)  
2. Clean data (handle missing fields, normalize names, remove duplicates) using `clean_materials_log.py`  
3. Validate entries (e.g. ensure all required fields are present) via `validate_entries.py`  
4. Aggregate data (count per material type, totals per chapter, weekly summaries) using `aggregate_materials_report.py`  
5. Export reports to `.xlsx` or `.csv` and generate charts for visualization  

## Tools Used
- Python (pandas, matplotlib/seaborn)  
- CSV, Excel  
- Basic plotting/charting  

## Sample Outputs
- Weekly summary: `reports/weekly_inventory_summary.xlsx`  
- Charts in `reports/charts/` showing trends and chapter distribution  

## How It Could be Used in the Real World
- Turn weekly CSVs provided by field teams into standardized reports  
- Supply dashboards to leadership for incentive tracking or material distribution  
- Automate alerts if any chapter falls below threshold counts  


