a = 1,
a = 1, 2
a, b = 1, 2

# Swap the values of two variables "a" and "b"
a = 1
b = 2

temp = a
a = b
b = temp
print(a)  # 2
print(b)  # 1

# Swap the values of two variables "a" and "b" using tuple packing and unpacking
a = 1
b = 2
a, b = b, a
print(a)  # 2
print(b)  # 1
