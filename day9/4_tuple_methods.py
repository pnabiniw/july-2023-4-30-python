# Tuples are immutable so we don't have the methods like append(), pop(), insert() etc. The only methods in
# tuples are count() and index()

vowels = ("a", "e", "i", "o", "u", "a", "u", "i")
result = vowels.count("a")
print(result)  # 2

result = vowels.index("a")  # 0
print(result)
result = vowels.index("a", 2, 7)  # 5
print(result)


# Some functions that can be used with tuple

# sum()
result = sum((1, 2, 3, 4, 5))
print(result)  # 15


# max()
print(max(1, 2, 3, 10, 20, 11, 3))  # 20

# min()
print(min(1, 2, 5, 0, -1))  # -1


# sorted()
a = (1, 2, 3, 10, 20, 11, 3)
print(sorted(a))   # [1, 2, 3, 3, 10, 11, 20]
print(sorted(a, reverse=True))   # [20, 11, 10, 3, 3, 2, 1]


# reversed()
a = (1, 2, 3, 10, 20, 11, 3)
print(reversed(a))  # <reverse_object>
result = reversed(a)
print(list(result))  # [3, 11, 20, 10, 3, 2, 1]


