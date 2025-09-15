## Overview
This project tracks the inventory and distribution of activism materials across chapters. It demonstrates a full data workflow: generating sample data, simulating messy field input, cleaning and validating, aggregating, and visualizing results.

## Motivation
Club America Administrators and field teams need to log and track activism materials for transparency, accountability, and timely restocking. This repo simulates that workflow with realistic sample data, cleaning, aggregation, validation, and reporting.

## Workflow
1. **Create sample data** in `data/materials_log_sample.csv`
2. **Generate messy raw data** using `generate_raw_data.py` → `data/materials_log_raw.csv`
3. **Clean and standardize** using `clean_materials_log.py` → `data/materials_log_clean.csv`
4. **Validate entries** with `validate_entries.py`
5. **Aggregate and visualize** using `aggregate_materials_report.py` → summary files and charts in `reports/`

## Tools Used
- Python (pandas, matplotlib, seaborn)
- CSV, Excel

## Sample Outputs
- Aggregated summaries: `reports/materials_by_chapter.xlsx`, `reports/materials_by_week.xlsx`, `reports/materials_by_type.xlsx`
- Charts: `reports/charts/materials_by_chapter.png`, etc.

## How It Could be Used in the Real World
- Turn weekly CSVs from field teams into standardized reports
- Supply dashboards to leadership for incentive tracking or material distribution
- Automate alerts if any chapter falls below threshold counts

---
This project is a template for tracking activism materials and demonstrating practical data cleaning, validation, and reporting skills.



Project
for
tracking
activism
materials.
