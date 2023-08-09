# Set in python are mutable datatype. However, every element of a set must be immutable
# Set doesn't support indexing and slicing
# Set elements are always unique
# Set are unordered. {1, 2} and {2, 1} are same.

# Creating an empty set
a = set()
# a = {} # This is not an empty set. It's an empty dictionary

# Creating non-empty set
data = {1, 2, 3, 4}
fruits = {"apple", "mango", "banana"}
a = {1, "a", (1, 2), 2.2}
print(a)
a = {[1, 2], 2}  # This is not a valid set. It raises error

