# String indexing and slicing is similar to that of List
# Forward indexing starts from 0 and reversing indexing starts from -1

# string indexing
message = "Hello World"
print(message[0])  # H
print(message[3])  # l
print(message[5])  # <space>
print(message[-1])  # d
print(message[-7])  # 0
print(message[20])  # It raises error; IndexError
print(message[-14])  # It also raises IndexError


# string slicing
message = "Hello World"
print(message[:5])  # "Hello"
print(message[0: 5])  # "Hello"
print(message[3:])  # "lo World"
print(message[2: 7])  # "llo W"
print(message[7: 2])  # ""

print(message[:-3])  # "Hello Wo"
print(message[0: -3])  # "Hello Wo"
print(message[-4:])  # "orld"
print(message[-2: -7])  # ""
print(message[-7: -2])  # "o Wor"
print(message[7: -8])  # ""
print(message[-8: 7])  # "lo W"

message = "Hello World"
# message[2] = "L"  # It raises error because we can't change the existing item in string as it is immutable
# del message[2]
del message  # it deletes the string


# Iterating through string
message = "Hello World"
for each in message:
    print(each)  # "H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"

for each in message[:5]:
    print(each)  # H, e, l, l, o
