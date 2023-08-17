# break, continue and pass are the control statements that can alter the normal
# flow of the program

for i in range(10):
    if i == 4:
        break
    print(i)

n = 0
while n <= 10:
    if n == 5:
        break
    print(n)
    n += 1


# continue
for i in range(10):
    if i == 5:
        continue
    print(i)  # 0, 1, 2, 3, 4 6, 7, 8, 9

n = 0
while n <= 10:
    if n == 5:
        n += 1
        continue
    print(n)  # 0, 1, 2, 3, 4, 6, 7, 8, 9, 10
    n += 1


# pass
def addition(a, b):
    pass   # Code comes here in future


class Student:
    pass  # Code comes here in future
