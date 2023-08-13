squared = []
for i in range(1, 6):
    squared.append(i**2)
print(squared)  # [1, 4, 9, 16, 25]

squared = [i**2 for i in range(1, 6)]
print(squared)
# This is list comprehension

squared_dict = {k: k**2 for k in range(1, 6)}
print(squared)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# This is an example of dictionary comprehension


student_list = [("name", "Jon"), ("age", 25), ("address", "KTM")]
student = dict(student_list)
print(student)

# {"name": "Jon", "age": 25, "address": "KTM"}
student = {key: value for key, value in student_list}  # Dictionary comprehension
print(student)
