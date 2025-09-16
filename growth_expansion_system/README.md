# Growth & Expansion System

This project analyzes chapter growth and expansion by tracking new student recruitment and active events over time. It includes realistic, messy data generation, cleaning, analysis, and visualization workflows.

## Data
- `data/growth_data_raw.csv`: Simulated raw data with inconsistencies and missing values.
- `data/growth_data_clean.csv`: Cleaned and standardized data for analysis.

## Scripts
- `scripts/generate_raw_growth_data.py`: Generates realistic, messy sample data.
- `scripts/clean_growth_data.py`: Cleans and standardizes the raw data.
- `scripts/analyze_growth_data.py`: Analyzes cleaned data and generates multiple visualizations.

## Reports & Visualizations
- `reports/`: Contains summary reports, pie and histogram charts.
- `reports/charts/`: Contains bar, line, scatter, and heatmap visualizations of growth metrics.

## Structure
- `data/` — Raw and processed data files
- `scripts/` — Python scripts for data generation, cleaning, and analysis
- `reports/` — Generated reports, summary charts, and PDFs
- `reports/charts/` — Detailed visualizations (bar, line, scatter, heatmap)
- `notebooks/` — Jupyter notebooks for interactive exploration

## Setup & Usage
1. Place your data files in the `data/` folder.
2. Run scripts in the `scripts/` folder to generate, clean, and analyze data.
3. Visualizations and reports will be saved in `reports/` and `reports/charts/`.
4. Use `notebooks/` for interactive analysis and custom exploration.

## Example Workflow
- Generate messy data: `python scripts/generate_raw_growth_data.py`
- Clean data: `python scripts/clean_growth_data.py`
- Analyze and visualize: `python scripts/analyze_growth_data.py`

---
For questions or improvements, open an issue or contribute via pull request.
