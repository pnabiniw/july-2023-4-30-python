# concatenation (+)
a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)  # (1, 2, 3, 4, 5, 6)


# Repetition / Broadcast (*)
a = (1, 2)
print(a * 2)  # (1, 2, 1, 2)

# Membership operation
print(1 in (1, 2, 3))  # True
print(3 not in (1, 2, 3))  # False


# Iteration in tuple is same as that of list
vowels = ("a", "e", "i", "o", "u")
for each in vowels:
    print(each)  # a, e, i, o, u

# Unlike list, tuple doesn't have tuple comprehension
a = [i for i in range(5)]  # this is list comprehension
print(a)
a = (i for i in range(5))  # This is generator expression (not tuple comprehension)



