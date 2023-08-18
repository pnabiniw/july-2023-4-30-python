# lambda are the elegant way of creating one-liner function
# Lambda functions do not have name. So, they are also called anonymous functions

def squared(num):
    return num ** 2

print(squared(2))  # 4

squared = lambda num: num ** 2
print(squared(4))  # 16


# map()
data = [1, 2, 3, 4]
result = map(lambda elem: elem ** 3, data)
print(list(result))
result = filter(lambda elem: elem ** 3, data)  # [1, 2, 3, 4]
print(list(result))  # [1, 8, 27, 64]


# filter()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x % 2 == 0, data)
print(list(result))
result = map(lambda x: x % 2 == 0, data)  # [False, True, False, True, False, True, False, True, False, True]
print(list(result))


# reduce()
from functools import reduce
data = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, data)
print(result)  # 15
