# Loops are used to execute certain blocks of code repeatedly
# They are used to reduce manual efforts in the algorithms

# for loops in python with different datatypes
vowels = ["a", "e", "i", "o", "u"]

for each in vowels:
    print(each)
else:
    print("This is executed if the main loop is completely iterated")

# looping is similar to list in tuple and set
# Let's see how is it done in a dictionary

student = {"name": "Jane", "age": 25, "address": "KTM"}

# Looping in dictionary keys
print(student.keys())  # dict_keys(["name", "age", "address"])

for key in student.keys():
    print(key)


# Looping in dictionary values
print(student.values())  # ["Jane", 25, "KTM"]
for value in student.values():
    print(value)


# Looping through both dictionary keys and values
print(student.items())  # dict_items([("name", "Jane"), ("age", 25), ("address", "KTM")])

for key, value in student.items():
    print(key)
    print(value)
