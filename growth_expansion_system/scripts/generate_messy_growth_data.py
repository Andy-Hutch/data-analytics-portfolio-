import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Simulate chapter names with typos and variations
chapter_variants = [
    'Phoenix HQ', 'Phx', 'phoenix', 'Phoenix', 'PHX', 'Phoenix Headquaters',
    'Tucson', 'Tuscon', 'Tucs', 'Tucson HQ', 'TUCSON',
    'Flagstaff', 'Flagstaf', 'Flag', 'Flagstaff HQ', 'FLAGSTAFF'
]

regions = ['SW', 'Southwest', 'north', 'North', 'N', 'S', '']

rows = []
for _ in range(200):
    # Messy date formats
    date_choice = random.choice([
        fake.date_between(start_date='-2y', end_date='today').strftime('%m/%d/%y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%b %d, %Y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%d-%b-%Y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%B %d %Y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%d/%m/%Y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%b %d %y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%d %b %Y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%m-%d-%Y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%d.%m.%Y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%Y/%m/%d'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%d %B %Y'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%b %d'),
        fake.date_between(start_date='-2y', end_date='today').strftime('%m/%d'),
    ])
    chapter = random.choice(chapter_variants)
    # Messy new_students
    new_students = random.choice([
        str(random.randint(0, 50)), '', '??', None, str(random.randint(0, 50)), str(random.randint(0, 50)), 'N/A'
    ])
    # Messy active_events
    active_events = random.choice([
        str(random.randint(0, 10)), '', None, 'unknown', str(random.randint(0, 10)), 'N/A', '0'
    ])
    region = random.choice(regions)
    notes = random.choice([
        '', fake.sentence(), 'anomaly', None, 'missing data', 'typo in chapter', 'extra event', '']
    )
    rows.append({
        'date': date_choice,
        'chapter': chapter,
        'new_students': new_students,
        'active_events': active_events,
        'region': region,
        'notes': notes
    })

messy_df = pd.DataFrame(rows)
messy_df.to_csv('../data/growth_data_raw.csv', index=False)
print('Messy dataset generated as data/growth_data_raw.csv')
