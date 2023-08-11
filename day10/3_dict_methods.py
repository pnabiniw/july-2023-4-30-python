# copy()
student = {"name": "Jon", "age": 12}
student1 = student.copy()
print(student)  # {"name": "Jon", "age": 12}
print(student1) # {"name": "Jon", "age": 12}


# get()
student = {"name": "Jon", "age": 12}
name = student.get("name")
print(name)  # Jon

name = student["name"]
print(name)  # Jon

roll = student.get('roll')  # None
# roll = student['roll']  # Error

roll = student.get("roll", 5)
print(roll)  # 5

name = student.get("name", "Jane")
print(name)  # Jon


# items()
student = {"name": "Jon", "age": 12}
print(student.items())  # dict_items([("name", "Jon"), ("age", 12)])

# keys()
student = {"name": "Jon", "age": 12}
print(student.keys())  # dict_keys(["name", "age"])

# values()
student = {"name": "Jon", "age": 12}
student.values()  # dict_values(["Jon", 12])

