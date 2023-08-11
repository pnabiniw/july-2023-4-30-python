# Membership Operation
# Dictionary membership is checked in keys and not in values
student = {"name": "Jon", "age": 25}

print("Jon" in student)  # False
print("name" in student)  # True
print("age" not in student)  # False


########## Built-in Functions #############
student = {"name": "Jon", "age": 25}

# len()
print(len(student))  # 2

# sorted()
result = sorted(student)
print(result)  # ["age", "name"]

# str()
result = str(student)
print(result)  # "{"name": "Jon", "age": 25}"


# all(sequence)
# all() function takes only one parameter and that should be an iterable
# All the elements inside the iterable must be truthy for all() to return True

data_list = [1, "Hello", [1, 2]]
result = all(data_list)
print(result)  # True

result = all([1, 2, 0])
print(result)  # False

# But there is one exception in all()
result = all([])
print(result)  # True


# any(sequence)
# any() function also takes only one parameter and that should be an iterable
# Any one element inside the iterable should be truthy for any() to return True

result = any([1, 0, False])
print(result)  # True

result = any([0, []])
print(result)  # False







