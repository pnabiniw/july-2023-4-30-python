# There are broadly two types of errors in Python
# 1. Syntactic Error
# 2. Non-Syntactic Error

# Syntactic errors occur when you mess up with the grammar of the Python
# Examples: Unwanted spaces, Indentation Error, Missed commas or colons etc


# All those errors except the syntax errors are non-syntactic errors
# They can further be classified as:
# 1. TypeError
# 2. ValueError
# 3. IndexError
# 4. KeyError
# 5. ZeroDivisionError
# 6. ModuleNotFoundError
# 7. AttributeError
# 8. NameError


# Examples
# print(2 + "Hello")  # TypeError
# int("hello")  # ValueError

# data = [1, 2, 3]
# print(data[10])  # IndexError

# student = {"name": "Hary", "age"40}
# print(student["address"])  # KeyError

# a = 2
# print(a / 0)  # ZeroDivisionError


# import mat  # ModuleNotFoundError

# a = [1, 2, 3]
# a.join(",")  # AttributeError. join() is string method

# nums = [1, 2, 3]
# print(num)  # NameError

