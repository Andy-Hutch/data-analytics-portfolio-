# Script to clean and standardize activism materials log data
import csv
import re
from datetime import datetime

input_path = 'activism_materials_tracking/data/materials_log_raw.csv'
output_path = 'activism_materials_tracking/data/materials_log_clean.csv'

# Normalization helpers
def normalize_date(date_str):
	if not date_str or date_str.strip() == '':
		return ''
	# Try multiple formats
	for fmt in ('%Y-%m-%d', '%m/%d/%y', '%b %d, %Y', '%d-%b-%Y', '%m/%d/%Y', '%d/%m/%Y', '%B %d %Y', '%d %B %Y'):
		try:
			return datetime.strptime(date_str.strip(), fmt).strftime('%Y-%m-%d')
		except Exception:
			continue
	return ''

def normalize_chapter(chapter):
	if not chapter:
		return ''
	chapter = chapter.strip().lower()
	if chapter in ['phx', 'phoenix', 'phx ', 'phx.', 'phx,']: return 'Phoenix'
	if chapter in ['tucson', 'tuc', 'tucs', 'tucs.']: return 'Tucson'
	return chapter.title()

def normalize_material(material):
	if not material:
		return ''
	material = material.strip().lower()
	if 'flyer' in material: return 'Flyers'
	if 'sticker' in material: return 'Stickers'
	if 'poster' in material: return 'Posters'
	if 'banner' in material: return 'Banners'
	if 'pamphlet' in material: return 'Pamphlets'
	if 'button' in material: return 'Buttons'
	return material.title()

def normalize_quantity(qty):
	if not qty or qty.strip() == '':
		return ''
	qty = qty.strip()
	if qty in ['??', '']: return ''
	if qty.lower() == 'one hundred': return '100'
	m = re.search(r'(\d+)', qty)
	if m:
		return m.group(1)
	return ''

def clean_row(row):
	cleaned = {
		'Date': normalize_date(row.get('Date', '')),
		'Material': normalize_material(row.get('Material', '')),
		'Quantity': normalize_quantity(row.get('Quantity', '')),
		'Location': normalize_chapter(row.get('Location', '')),
		'Contact': row.get('Contact', '').strip().title(),
		'Notes': row.get('Notes', '').strip()
	}
	# Force-fill every row
	cleaned['Quantity'] = cleaned['Quantity'] if cleaned['Quantity'] and cleaned['Quantity'].strip() != '' else '0'
	cleaned['Notes'] = cleaned['Notes'] if cleaned['Notes'] and cleaned['Notes'].strip() != '' else 'N/A'
	return cleaned

with open(input_path, 'r', encoding='utf-8') as fin, open(output_path, 'w', newline='', encoding='utf-8') as fout:
	reader = csv.DictReader(fin)
	fieldnames = ['Date', 'Material', 'Quantity', 'Location', 'Contact', 'Notes']
	writer = csv.DictWriter(fout, fieldnames=fieldnames)
	writer.writeheader()
	for row in reader:
		# Ensure all expected fields are present
		for key in fieldnames:
			if key not in row:
				row[key] = ''
		cleaned = clean_row(row)
		writer.writerow(cleaned)
# Script to clean messy activism materials log data
import csv
import re
from datetime import datetime

input_path = 'activism_materials_tracking/data/materials_log_raw.csv'
output_path = 'activism_materials_tracking/data/materials_log_clean.csv'

# Normalization helpers
def normalize_date(date_str):
	for fmt in ('%d/%m/%Y', '%Y-%m-%d', '%m/%d/%Y'):
		try:
			return datetime.strptime(date_str.strip(), fmt).strftime('%Y-%m-%d')
		except Exception:
			continue
	return ''

def normalize_material(material):
	material = material.strip().lower().replace('3', 'e')
	material = material.replace('flyers', 'Flyers').replace('posters', 'Posters')
	material = material.replace('stickers', 'Stickers').replace('banners', 'Banners')
	material = material.replace('pamphlets', 'Pamphlets').replace('buttons', 'Buttons')
	# Remove extra whitespace
	return material.title().strip()

def normalize_location(location):
	location = location.strip().title()
	if location in ('', 'Unknown'):
		return 'Unknown'
	if location.startswith('Hq'):
		return 'HQ'
	return location

def normalize_contact(contact):
	contact = contact.strip().title()
	if contact == '':
		return 'Unknown'
	return contact

def normalize_quantity(qty):
	if not qty or qty.strip() == '':
		return ''
	qty = qty.replace('pcs', '').replace(' ', '')
	try:
		return str(int(qty))
	except Exception:
		# Try to extract number
		m = re.search(r'(\d+)', qty)
		if m:
			return m.group(1)
		return ''

def clean_row(row):
	return {
		'Date': normalize_date(row.get('Date', '')),
		'Material': normalize_material(row.get('Material', '')),
		'Quantity': normalize_quantity(row.get('Quantity', '')),
		'Location': normalize_location(row.get('Location', '')),
		'Contact': normalize_contact(row.get('Contact', '')),
		'Notes': row.get('Notes', '').strip()
	}

with open(input_path, 'r', encoding='utf-8') as fin, open(output_path, 'w', newline='', encoding='utf-8') as fout:
	reader = csv.DictReader(fin)
	fieldnames = ['Date', 'Material', 'Quantity', 'Location', 'Contact', 'Notes']
	writer = csv.DictWriter(fout, fieldnames=fieldnames)
	writer.writeheader()
	for row in reader:
		cleaned = clean_row(row)
		writer.writerow(cleaned)
