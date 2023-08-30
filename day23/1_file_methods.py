filename = "message.txt"

# with open(filename, "w") as fp:
#     fp.write("Hello World\nI'm Learning Python")


# read()
# seek()
# readline()
# readlines()
# tell()
# writelines()
with open(filename, "r") as fp:
    data = fp.read()
    print(data)   # Hello World I'm Learning Python

    fp.seek(0)  # seek() method changes the cursor of the file
    data = fp.read(7)  # Hello W
    print(data)

    fp.seek(0)
    data = fp.readline()
    print(data)   # Hello World

    fp.seek(0)
    data = fp.readlines()
    print(data)   # ["Hello World\n", "I'm Learning Python"]


data = ["Hello World\n", "I'm Learning Python\n", "Python is a high level language"]
with open(filename, 'w') as fp:
    fp.writelines(data)
