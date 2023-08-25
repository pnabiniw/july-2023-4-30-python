# We can open, close, read, write or perform any other kind of work with file using Python
# There are several modes from which we can open a file

# r => read file
# w => write in the file
# a => append mode
# r+ => read and write mode
# w+ => write and read mode
# x => exclusive write mode
# a+ => append and read mode

filename = "message.txt"
fp = open(filename, "w")
fp.write("Hello World")
fp.close()


fp = open(filename, "r")
data = fp.read()
print(data)
print(type(data))  # string
fp.close()

# Closing the file is important as it protects the system from memory leakage.
# But sometimes we may forget to close the file
# So, it is better to open a file with context manager

with open(filename, "a") as fp:  # context manager
    fp.write("\nI'm learning python")


with open(filename, "r+") as fp:
    data = fp.read()
    print(data)
    fp.seek(0)  # it puts the file pointer to the top of the file
    fp.write("Python is a high level language")


with open(filename, "w+") as fp:
    fp.write("I'm learning Python")
    fp.seek(0)
    data = fp.read()
    print(data)


with open(filename, "x") as fp:
    fp.write("Hello World. I'm learning Python")
