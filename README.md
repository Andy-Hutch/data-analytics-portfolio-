# Chapter Incentive Program Data Analytics

This project demonstrates a simple data analytics workflow for a chapter incentive program. It includes scripts to generate synthetic data, clean it, and perform basic analysis.

## Project Structure

- `data/` — Contains raw and cleaned incentive data CSV files
- `scripts/` — Python scripts for data generation, cleaning, and analysis
- `reports/` — (Optional) For storing analysis reports or visualizations

## Workflow

1. **Generate Raw Data**
	- Run `scripts/generate_raw_incentive_data.py` to create synthetic incentive data in `data/incentive_data_raw.csv`.

2. **Clean the Data**
	- Run `scripts/clean_incentive_data.py` to clean the raw data and save results to `data/incentive_data_clean.csv`.

3. **Analyze the Data**
	- Run `scripts/analyze_incentive_data.py` to print summary statistics and breakdowns by chapter, program, and month.

## Requirements

- Python 3.x
- pandas

Install dependencies:
```
pip install pandas
```

## Usage

Run each script from the project root directory:
```
python scripts/generate_raw_incentive_data.py
python scripts/clean_incentive_data.py
python scripts/analyze_incentive_data.py
```
