# If a function is called from the definition of the same function then it is called as a recursive function

c = 0


def count():
    global c
    print(c)
    if c == 10:
        return
    c += 1
    count()


count()



# WAP to calculte the factorial of 5 in three ways:
# Normal loop
# reduce() function
# recursion


# Normal Loop
fact = 1
for i in range(1, 6):
    fact = fact * i
print(fact)


# reduce()
from functools import reduce
result = reduce(lambda x, y: x * y, range(1, 6))
print(result)


# recursion

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)


result = factorial(5)
print(result)


# 5 * factorial(4)   => 5 * 24 = 120
# 4 * factorial(3)  => 4 * 6 = 24
# 3 * factorial(2)  => 3 * 2 = 6
# 2 * factorial(1)   => 2 * 1 = 2
# 1 * factorial(0)  => 1 * 1 = 1
