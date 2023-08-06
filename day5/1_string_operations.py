# Concatenation => We can concatenate strings using "+" operator

m1 = "Hello"
m2 = "World"
print(m1 + m2)  # HelloWorld


# Repetition / Broadcast Operation => Broadcast in string is done using * operator
message = "Hello"
print(message * 3)  # HelloHelloHello


# Membership operation
print("m" in "message")  # True
print("e" not in "message")  # False


# Built-in functions
# 1. len() => It gives the length (total number of elements) of sequential datatypes
# i.e. list, string, tuple etc
message = "Hello World"
print(len(message))  # 11

# 2. type() => returns the type of any object
print(type(message))  # <class "str">

# slice() => this function is similar to string and list slicing

sliced_data = slice(2, 7)
print(message[sliced_data])  # llo W









