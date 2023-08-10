# Dictionary are the mutable datatype in python in key-value pair format

# Creating an empty dictionary
a = dict()
print(a)  # empty dictionary
a = {}
print(a)  # empty dictionary


# Creating non-empty dictionary
student = {"name": "Ram", "age": 25, "address": "KTM"}
print(student)  # {"name": "Ram", "age": 25, "address": "KTM"}

student = dict(name="Jon", age=23, address="KTM")
print(student)  # {"name": "Jon", "age": 23, "address": "KTM"}


data = {"phone number": "9878989879"}
data = dict(phone_number=9890989098)
print(data)

data = dict({"name": "Ram", "age": 25, "address": "KTM"})
print(data)
