# JSON stands for JavaScript Object Notation
# JSON is a file format with .json extension which is used to share data and information over the
# internet
# Python has a built-in module for json handling
# JSON is similar to python dictionary as it is also written in key-value format. But, keys and values
# in JSON data must be enclosed in double-quotes. Single quotes are not allowed

# Integers and float values do not require quotes in JSON

# Some examples of JSON data
{"name": "Hary", "age": 30, "address": "KTM"}  # Valid JSON
{'name': 'Hary', 'age': 30, 'address': 'KTM'}  # Invalid JSON because of the single quotes

[
    {"name": "Hary", "age": 30, "address": "KTM"},
    {"name": "Jon", "age": 25, "address": "PKR"}
]   # Valid JSON


import json
filename = "students.json"
student = {'name': 'Hary', "age": 30, "address": "KTM"}
students = [
    {"name": "Hary", "age": 30, "address": "KTM"},
    {"name": "Jon", "age": 25, "address": "PKR"}
]

with open(filename, "w+") as fp:
    data = json.dumps(students, indent=2)
    fp.write(data)
    fp.seek(0)
    data = json.loads(fp.read())
    print(type(data))

name = data[1]["name"]
