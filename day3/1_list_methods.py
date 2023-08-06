# append()
vowels = ["a", "e", "i", "o"]
result = vowels.append("u")
print(result)
print(vowels)

# extend()
a = [1, 2, 3]
b = [4, 5, 6]
result = a.extend(b)
print(result)  # None
print(a)   # [1, 2, 3, 4, 5, 6]


# insert(index, value)
vowels = ["a", "e", "o", "u"]
vowels.insert(2, "i")
print(vowels)


# remove(value)
a = [1, 2, 3, 4, 5]
a.remove(3)
print(a)
# a.remove(6)   # It raises ValueError


# pop(index)
vowels = ["a", "e", "i", "o", "u"]
result = vowels.pop(1)
print(result)   # e
print(vowels)  # [a, i, o, u]

# pop() method doesn't necessarily take a parameter. If parameter not provided then last item from the
# list is popped out.


# clear()
a = [1, 2, 3, 4]
a.clear()
print(a)  # []


# index(value, start, end)
vowels = ["a", "e", "i", "o", "u"]
result = vowels.index("i")
print(result)

a = [1, 2, 3, 4, 1, 4, 5, 2, 3, 2]
result = a.index(2, 2)
print(result)  # 7

result = a.index(1, 2, 8)
print(result)  # 4


# count()
a = [1, 2, 3, 1, 2, 4, 2, 3, 3, 1, 1]
print(a.count(3))  # 3
print(a.count(1))  # 4


# reverse()
a = [2, 1, 10, 9, 3]
a.reverse()
print(a)   # [3, 9, 10, 1, 2]
