# while loop is another way to loop in python. "while" takes a statement after it and the loop runs
# until this statement is truthy. It stops immediately on getting falsy statement

n = 0
while n <= 10:
    print(n)
    n += 1
else:
    print("This is executed when the loop is completely iterated")

while True:
    print("Hello")


