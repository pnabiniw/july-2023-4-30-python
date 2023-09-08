"""
1. What are the methods to get keys, values and key-value pair in dictionary?
2. How to loop in key-value pair?

"""

student = {"name": "ram", "age": 30}
student.keys()
student.values()
student.items()


# [("name", "ram"), ("age": 30)]

for key, value in student.items():
    print(key)
    print(value)
