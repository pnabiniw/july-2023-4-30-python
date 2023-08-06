# Python list are mutable data-types and are sequential (also an iterable).
# Lists are created enclosing data in big brackets [] or using built-in function list()

# Creating an empty list
a = []
b = list()

# Creating non-empty list
a = [1, 2, 3]
vowels = ["a", "e", "i", "o", "u"]
# The above are the examples of list with homogenous data-types


# List can also contain heterogenous types
a = [1, 2.3, ["a", "e"], ("i", 3), {1, 2, 3}, {"a": 1, "b": 2}]  # list with multiple types



###################### Accessing List Items ###########################
# List items can be accessed using indexing and slicing

# Indexing in list starts from 0 for forward traverse and -1 for reverse traverse
vowels = ["a", "e", "i", "o", "u"]
print(vowels)
print(vowels[0])  # a
print(vowels[2])  # i
print(vowels[4])  # u

print(vowels[-1])  # u
print(vowels[-3])  # i

# print(vowels[10])  # IndexError: list index out of range
# print(vowels[-8])  # IndexError: list index out of range


# Item assignment is possible in list as it is mutable
vowels[1] = "E"
print(vowels)


# List Slicing
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(a[0:5])  # ["a", "b", "c", "d", "e"]
print(a[:5])  # ["a", "b", "c", "d", "e"]
print(a[2:])  # ["c", "d", "e", "f", "g", "h", "i", "j"]

print(a[2: 7])  # ["c", "d", "e", "f", "g"]
print(a[7: 2])  # []

print(a[0: -2])  # ["a", "b", "c", "d", "e", "f", "g", "h"]
print(a[:-2])  # ["a", "b", "c", "d", "e", "f", "g", "h"]
print(a[-5:])  # ["f", "g", "h", "i", "j"]

print(a[-7: -2])  # ["d", "e", "f", "g", "h"]
print(a[-2: -7])  # []

print(a[2: -1])  # ["c", "d", "e", "f", "g", "h", "i"]



# List Operations

# Concatenation
a = [1, 2, 3]
b = [4, 5, 6]
result = a + b
print(result)  # [1, 2, 3, 4, 5, 6]


# Membership Operation
print(2 in [1, 2, 3])  # True
print(3 not in [1, 2, 3])  # False








