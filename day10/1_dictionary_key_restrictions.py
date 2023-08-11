# Dictionary keys has a restriction that they must be immutable datatype
# There is no such restriction in dictionary values

a = {"name": "Jon", "age": 25}  # Valid
b = {1: "Hello", 2: "World"}  # Valid
c = {2.45: 1, 2.3: 2}  # Valid
d = {(1, 2): "Hello", (3, 2): "World"}  # Valid
e = {[1, 2]: 1, [3, 1]: 8}  # Invalid
f = {([1, 2], 3): 5, "name": "Jon"}  # Invalid
