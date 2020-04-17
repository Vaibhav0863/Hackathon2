import csv

def pull(file_path):
	with open(file_path) as file:
		reader = csv.DictReader(file)

		data = []

		for row in reader:
			data.append(row)

		return data

def push(file_path,data):
	fieldnames = data.pop(0)
	with open(file_path,'w') as file:
		writer = csv.DictWriter(file,fieldnames=fieldnames)
		writer.writeheader()
		for row in data:
			writer.writerow(row)

	print("UPLOADED SUCCESSFULLY...")

def pushF(file_path,data):
	fieldnames = data[0].keys()
	with open(file_path,'w') as file:
		writer = csv.DictWriter(file,fieldnames=fieldnames)
		writer.writeheader()
		for row in data:
			writer.writerow(row)

	print("UPLOADED SUCCESSFULLY...")

