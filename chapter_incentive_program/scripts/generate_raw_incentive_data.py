import csv
import random
from datetime import datetime, timedelta

# Configuration
num_records = 500
output_file = 'data/incentive_data_raw.csv'

# Sample data pools
chapters = [f'Chapter {i}' for i in range(1, 21)]
programs = ['Referral', 'Sales', 'Engagement', 'Retention']

# Helper function to generate random dates in 2025
def random_date():
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Generate data
rows = []
for _ in range(num_records):
    chapter = random.choice(chapters)
    program = random.choice(programs)
    member_id = f'M{random.randint(1000, 9999)}'
    incentive_amount = round(random.uniform(10, 500), 2)
    date_awarded = random_date()
    rows.append([chapter, program, member_id, incentive_amount, date_awarded])

# Write to CSV
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Chapter', 'Program', 'MemberID', 'IncentiveAmount', 'DateAwarded'])
    writer.writerows(rows)

print(f"Generated {num_records} records in {output_file}")
