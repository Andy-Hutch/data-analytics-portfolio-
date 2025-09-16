import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Generate sample data
np.random.seed(0)
dates = [datetime.now() - timedelta(days=i) for i in range(30)]
chapters = ['Phoenix', 'Tucson', 'Flagstaff', 'Yuma']
new_students = np.random.randint(5, 20, size=30)
active_events = np.random.randint(0, 3, size=30)
regions = np.random.choice(['Southwest', 'Northern AZ'], size=30)
notes = ['' for _ in range(30)]

data = {
    'date': np.random.choice(dates, size=30),
    'chapter': np.random.choice(chapters, size=30),
    'new_students': new_students,
    'active_events': active_events,
    'region': regions,
    'notes': notes
}

df = pd.DataFrame(data)
df['new_students'] = df['new_students'].astype('object')

# Introduce some inconsistencies
df.loc[5, 'chapter'] = 'PHX'
df.loc[10, 'new_students'] = '??'
df.loc[15, 'date'] = '2025-08-15'
df.loc[20, 'region'] = 'SW'

# Save to CSV
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_dir, exist_ok=True)
csv_path = os.path.join(data_dir, 'growth_data_raw.csv')
df.to_csv(csv_path, index=False)
