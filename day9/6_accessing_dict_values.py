# Accessing elements of dictionary is similar to that of list. In list we put numbers for indexing and in
# dictionary we put "keys" for indexing

student = {"name": "Jane", "age": 25, "address": "KTM"}
name = student["name"]
print(name)  # Jane

age = student["age"]
print(age)  # 25

address = student["address"]
print(address)  # KTM

# phone = student["phone"]  # KeyError

# We can also access dictionary values using get() method
name = student.get("name")
print(name)  # Jane

phone = student.get("phone")  # It doesn't raise error. It gives None


# Adding a key-value pair in dictionary
student = {"name": "Jane", "age": 25, "address": "KTM"}
student["phone"] = "9890989878"
print(student)  # {"name": "Jane", "age": 25, "address": "KTM", "phone": "9890989878}


other_info = {"email": "a@a.com", "roll": 12}
student.update(other_info)
print(student)  # {"name": "Jane", "age": 25, "address": "KTM", "phone": "9890989878, "email": "a@a.com", "roll": 12}


student["name"] = "Jon"
print(student)  # {"name": "Jon", "age": 25, "address": "KTM", "phone": "9890989878", "email": "a@a.com", "roll": 12}



# Removing key-value pair from a dictionary
student = {"name": "Jon", "age": 25, "address": "KTM", "phone": "9890989878", "email": "a@a.com", "roll": 12}

email = student.pop("email")
print(student)  # {"name": "Jon", "age": 25, "address": "KTM", "phone": "9890989878", "roll": 12}
print(email)  # a@a.com

# institution = student.pop("institution")  # It raises KeyError
institution = student.pop("institution", 'Broadway')
print(institution)  # Broadway


# popitem()
student = {"name": "Jon", "age": 25, "address": "KTM", "phone": "9890989878", "email": "a@a.com", "roll": 12}
result = student.popitem()
print(result)  # ("roll", 12)
print(student)  # {"name": "Jon", "age": 25, "address": "KTM", "phone": "9890989878", "email": "a@a.com"}


student.clear()
print(student)  # {}


