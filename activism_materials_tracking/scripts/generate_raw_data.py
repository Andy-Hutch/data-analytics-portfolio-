# This script generates a messy CSV dataset for activism materials tracking
import csv
import random
from datetime import datetime, timedelta

output_path = '../data/materials_log_raw.csv'

materials = ['Flyers', 'Posters', 'Stickers', 'Banners', 'Pamphlets', 'Buttons']
locations = ['HQ', 'Warehouse', 'Field', 'Event', 'Unknown', '']
names = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Jamie', 'Pat', '']

def random_date():
	start = datetime(2024, 1, 1)
	end = datetime(2025, 9, 1)
	delta = end - start
	random_days = random.randint(0, delta.days)
	date = start + timedelta(days=random_days)
	# Sometimes return in different formats
	if random.random() < 0.2:
		return date.strftime('%d/%m/%Y')
	elif random.random() < 0.2:
		return date.strftime('%Y-%m-%d')
	else:
		return date.strftime('%m/%d/%Y')

def random_quantity():
	# Sometimes as string, sometimes as int, sometimes missing
	if random.random() < 0.1:
		return ''
	elif random.random() < 0.2:
		return str(random.randint(1, 100)) + ' pcs'
	else:
		return str(random.randint(1, 100))

def random_material():
	# Sometimes misspelled or extra whitespace
	m = random.choice(materials)
	if random.random() < 0.1:
		m = m.lower()
	if random.random() < 0.1:
		m = m + ' '
	if random.random() < 0.05:
		m = m.replace('e', '3')
	return m

def random_location():
	loc = random.choice(locations)
	if random.random() < 0.1:
		loc = loc + ' '
	return loc

def random_name():
	n = random.choice(names)
	if random.random() < 0.1:
		n = n.upper()
	return n

def random_note():
	notes = [
		'',
		'urgent',
		'damaged',
		'restock needed',
		'delivered late',
		'partial shipment',
		'']
	return random.choice(notes)

rows = []
for i in range(100):
	row = {
		'Date': random_date(),
		'Material': random_material(),
		'Quantity': random_quantity(),
		'Location': random_location(),
		'Contact': random_name(),
		'Notes': random_note()
	}
	# Randomly shuffle columns or add extra columns
	if random.random() < 0.1:
		row['Extra'] = '???'
	rows.append(row)

fieldnames = ['Date', 'Material', 'Quantity', 'Location', 'Contact', 'Notes', 'Extra']

with open(output_path, 'w', newline='', encoding='utf-8') as f:
	writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
	writer.writeheader()
	for row in rows:
		writer.writerow(row)
