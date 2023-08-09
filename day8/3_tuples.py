# Tuples are immutable data type. They are sequential datatype
# Elements in tuple are enclosed in parenthesis (small brackets)

# Creating an empty tuple
a = tuple()
print(a)  # empty tuple
a = ()
print(a)  # empty tuple


# Creating non-empty tuple
a = (1, 2, 3)
print(a)
a = tuple([1, 2, 3])
print(a)
a = ([1, 2], 1, "a", {"1": 2})
print(a)

a = 1
print(type(a))  # int
a = (1)
print(type(a))  # int
a = (1,)
print(a)  # (1,) => tuple
a = 1,
print(a)  # (1,)
print(type(a))  # tuple
