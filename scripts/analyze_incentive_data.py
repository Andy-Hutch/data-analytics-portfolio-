import pandas as pd

# Input file path
input_file = 'data/incentive_data_clean.csv'

# Read cleaned data
df = pd.read_csv(input_file)

# 1. Summary statistics
total_records = len(df)
total_incentive = df['IncentiveAmount'].sum()
avg_incentive = df['IncentiveAmount'].mean()

# 2. Incentive by Chapter
incentive_by_chapter = df.groupby('Chapter')['IncentiveAmount'].sum().sort_values(ascending=False)

# 3. Incentive by Program
incentive_by_program = df.groupby('Program')['IncentiveAmount'].sum().sort_values(ascending=False)

# 4. Incentive over time (monthly)
df['Month'] = pd.to_datetime(df['DateAwarded']).dt.to_period('M')
incentive_by_month = df.groupby('Month')['IncentiveAmount'].sum()

# Print results
print(f"Total records: {total_records}")
print(f"Total incentive amount: ${total_incentive:,.2f}")
print(f"Average incentive amount: ${avg_incentive:,.2f}\n")

print("Incentive Amount by Chapter:")
print(incentive_by_chapter)
print("\nIncentive Amount by Program:")
print(incentive_by_program)
print("\nIncentive Amount by Month:")
print(incentive_by_month)

# Save summary tables as CSV files in reports/
incentive_by_chapter.to_csv('reports/incentive_by_chapter.csv', header=True)
incentive_by_program.to_csv('reports/incentive_by_program.csv', header=True)
incentive_by_month.to_csv('reports/incentive_by_month.csv', header=True)

# Save summary statistics as a CSV
summary_stats = pd.DataFrame({
	'TotalRecords': [total_records],
	'TotalIncentive': [total_incentive],
	'AverageIncentive': [avg_incentive]
})
summary_stats.to_csv('reports/summary_statistics.csv', index=False)

# Export summary statistics and tables as a PDF report
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

pdf_file = 'reports/incentive_report.pdf'
doc = SimpleDocTemplate(pdf_file, pagesize=letter)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph('Chapter Incentive Program Analysis Report', styles['Title']))
elements.append(Spacer(1, 12))

# Summary statistics
summary_data = [
	['Total Records', total_records],
	['Total Incentive Amount', f"${total_incentive:,.2f}"],
	['Average Incentive Amount', f"${avg_incentive:,.2f}"]
]
summary_table = Table(summary_data)
summary_table.setStyle(TableStyle([
	('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
	('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
	('ALIGN', (0, 0), (-1, -1), 'LEFT'),
	('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
	('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))
elements.append(Paragraph('Summary Statistics', styles['Heading2']))
elements.append(summary_table)
elements.append(Spacer(1, 12))

# Incentive by Chapter
chapter_data = [['Chapter', 'Total Incentive Amount']]
chapter_data += [[ch, f"${amt:,.2f}"] for ch, amt in incentive_by_chapter.items()]
chapter_table = Table(chapter_data)
chapter_table.setStyle(TableStyle([
	('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
	('ALIGN', (0, 0), (-1, -1), 'LEFT'),
	('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
	('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))
elements.append(Paragraph('Incentive Amount by Chapter', styles['Heading2']))
elements.append(chapter_table)
elements.append(Spacer(1, 12))

# Incentive by Program
program_data = [['Program', 'Total Incentive Amount']]
program_data += [[pr, f"${amt:,.2f}"] for pr, amt in incentive_by_program.items()]
program_table = Table(program_data)
program_table.setStyle(TableStyle([
	('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
	('ALIGN', (0, 0), (-1, -1), 'LEFT'),
	('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
	('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))
elements.append(Paragraph('Incentive Amount by Program', styles['Heading2']))
elements.append(program_table)
elements.append(Spacer(1, 12))

# Incentive by Month
month_data = [['Month', 'Total Incentive Amount']]
month_data += [[str(m), f"${amt:,.2f}"] for m, amt in incentive_by_month.items()]
month_table = Table(month_data)
month_table.setStyle(TableStyle([
	('BACKGROUND', (0, 0), (-1, 0), colors.lightyellow),
	('ALIGN', (0, 0), (-1, -1), 'LEFT'),
	('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
	('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))
elements.append(Paragraph('Incentive Amount by Month', styles['Heading2']))
elements.append(month_table)

doc.build(elements)
print(f"PDF report saved to {pdf_file}")

# Generate and save charts as images in reports/
import matplotlib.pyplot as plt

# Incentive by Chapter (bar chart)
plt.figure(figsize=(10,6))
incentive_by_chapter.plot(kind='bar', color='skyblue')
plt.title('Total Incentive Amount by Chapter')
plt.ylabel('Incentive Amount ($)')
plt.xlabel('Chapter')
plt.tight_layout()
plt.savefig('reports/incentive_by_chapter.png')
plt.close()

# Incentive by Program (bar chart)
plt.figure(figsize=(8,5))
incentive_by_program.plot(kind='bar', color='lightgreen')
plt.title('Total Incentive Amount by Program')
plt.ylabel('Incentive Amount ($)')
plt.xlabel('Program')
plt.tight_layout()
plt.savefig('reports/incentive_by_program.png')
plt.close()

# Incentive by Month (line chart)
plt.figure(figsize=(10,6))
incentive_by_month.plot(kind='line', marker='o', color='orange')
plt.title('Total Incentive Amount by Month')
plt.ylabel('Incentive Amount ($)')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/incentive_by_month.png')
plt.close()

print("Charts saved as images in the reports folder.")
