import csv

filename = "students.csv"
result = []
with open(filename, "r") as cr:
    csv_reader = csv.DictReader(cr)
    for each in csv_reader:
        result.append(each)
print(result)



"""
{'id': '1', 'name': 'Jon', 'age': '30', 'address': 'KTM'}
{'id': '2', 'name': 'Jane', 'age': '45', 'address': 'PKR'}
{'id': '3', 'name': 'Ken', 'age': '21', 'address': 'BKT'}
"""