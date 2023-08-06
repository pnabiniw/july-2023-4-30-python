# We can loop (for loop) through the list in following way:

a = [1, 2, 3, 4]
for i in a:
    print(i)

# [1, 4, 9, 16]
b = list()
for i in a:
    value = i**2  # 1, 4, 9, 16
    b.append(value)  # [1, 4, 9, 16]

print(b)
print(a)

b = [i**2 for i in a]  # This is list comprehension
print(b)
