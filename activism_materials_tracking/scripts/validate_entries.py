# Script to validate cleaned activism materials log data
import csv
import sys

input_path = 'activism_materials_tracking/data/materials_log_clean.csv'

def is_missing(row, field):
	value = row.get(field, '').strip()
	if field == 'Quantity':
		return value == ''
	if field == 'Notes':
		return value == ''
	return value == ''

def is_duplicate(row, seen):
	key = (row['Date'], row['Material'], row['Location'], row['Contact'])
	if key in seen:
		return True
	seen.add(key)
	return False

def is_invalid_quantity(qty):
	try:
		return int(qty) < 0
	except:
		return True

def validate():
	with open(input_path, 'r', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		seen = set()
		errors = []
		required_fields = [f for f in reader.fieldnames if f not in ('Quantity', 'Notes')]
		for i, row in enumerate(reader, 2):
			missing = [field for field in required_fields if is_missing(row, field)]
			if missing:
				errors.append(f"Row {i}: Missing fields: {', '.join(missing)}")
			if is_duplicate(row, seen):
				errors.append(f"Row {i}: Duplicate entry")
			if row.get('Quantity') and is_invalid_quantity(row['Quantity']):
				errors.append(f"Row {i}: Invalid quantity: {row['Quantity']}")
		if errors:
			print("Validation errors found:")
			for err in errors:
				print(err)
		else:
			print("All entries are valid.")

if __name__ == "__main__":
	validate()

