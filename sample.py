data = [
{'id':3,'name':'Bala'},
{'id':1,'name':'vaibhav'},
{'id':2,'name':'Omkar'}
]


data = sorted(data,key = lambda row:[row['name'],int(row['id'])])

for row in data:
	print(row)