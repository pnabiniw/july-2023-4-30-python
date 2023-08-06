# True and False are the boolean data-types in Python. Keywords "True" and "False" are used to
# represent true state and false state respectively


########## Operations that give boolean type #############
# 1. Comparison Operation
a = 5
b = 3
print(a > b)   # True
print(a < b)   # False
print(a == b)  # False
print(a >= b)  # True
print(a <= b)  # False
print(b != a)  # True


# Logical Operation
a = 5
b = 3
print(a > b and b != a)  # True
print(a != b or a > b)  # True
print(not True)  # False
print(not False)  # True

print(not a)  # False


# Membership Operation
print("a" in ["a", "e", "i"])  # True
print("i" not in ["a", "e", "i"])  # False

# Identity Operation
a = 1
b = 1
print(a is b)  # True
print(id(a) == id(b))  # True
print(a is not b)  # False
print(id(a) != id(b))  # False



###### Concept of Truthy and Falsy ##################
a = 5
print(not a)  # False

# Any non-zero or non-empty data-type including True itself is a truthy data type
# 5, 1, -23, [1, 2], (4, 5), {-4, -5, "a"}, {"a": 1}, True; all these data are truthy data types

# In contrast, all empty data-types, zero and None including False are Falsy datatypes
# 0, [], (), {}, set(), '', None, False; all these data are Falsy data types

# How can we verify data is Truthy or Falsy?
# We can use bool() built-in function

# Check for truthy
a = 4
b = -3
c = [1, 2, 3]
d = (1, 2)
e = {1, 2}
f = {"a": 1}
g = "Hello World"
h = True
print(bool(a))  # True
print(bool(b))  # True
print(bool(c))  # True
print(bool(d))  # True
print(bool(e))  # True
print(bool(f))  # True
print(bool(g))  # True
print(bool(h))  # True

# Applying not operation to any truthy value results in False
print(not a)  # False


# Check for falsy
a = 0
b = []
c = ()
d = {}
f = set()
g = ''
h = None
i = False

print(bool(a))  # False
print(bool(b))  # False
print(bool(c))  # False
print(bool(d))  # False
print(bool(e))  # False
print(bool(f))  # False
print(bool(g))  # False
print(bool(h))  # False
print(bool(i))  # False
print(bool())   # False

# Applying not operation to any falsy value results in True
print(not a)  # True
print(not None)  # True



########## Python Boolean is a Sub-class of Integer #############
# True is integer 1 and False is integer 0

print(True + 1)  # 2
print(70 * False)  # 0
print(True + True)  # 2
print(True + False)  # 1
