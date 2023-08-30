import csv
students = [
    {'id': '1', 'name': 'Jon', 'age': '30', 'address': 'KTM'},
    {'id': '2', 'name': 'Jane', 'age': '45', 'address': 'PKR'},
    {'id': '3', 'name': 'Ken', 'age': '21', 'address': 'BKT'},
    {'id': '4', 'name': 'Ram', 'age': '34', 'address': 'BKT'},
    {'id': '5', 'name': 'Raj', 'age': '22', 'address': 'BKT'},
]

filename = "students_write.csv"

with open(filename, "w") as cw:
    field_names = students[0].keys()  # dict_values(['id', "name", "age", "address"])
    csv_writer = csv.DictWriter(cw, fieldnames=field_names)
    csv_writer.writeheader()
    for student in students:
        if student["age"] <= "25":
            csv_writer.writerow(student)
