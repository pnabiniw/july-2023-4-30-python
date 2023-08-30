# CSV stands for Comma Separated Values
# CSV files have extension .csv
import csv

filename = "students.csv"
with open(filename, "r") as cr:
    # csv_reader = csv.reader(cr)
    result = []
    for count, each_line in enumerate(csv.reader(cr)):
        print(each_line)
        if count == 0:
            continue
        data = dict(id=each_line[0], name=each_line[1], age=each_line[2], address=each_line[3])
        result.append(data)

print(result)


"""
["id", "name", "address"]
[1, "Jon", "KTM"]
[2, "Jane", "PKR"]
[3, "Ken", "BKT"]
"""

"""[
    {"id": 1, "name": "Jon", "address": "KTM"},
    {"id": 2, "name": "Jane", "address": "PKR"},
    {"id": 3, "name": "Ken", "address": "BKT"},
]"""
