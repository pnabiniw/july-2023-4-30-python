# A function that takes another function as an argument is called higher order function
# sorted(), map(), filter(), reduce(), decorators etc. are the higher order functions in python

# map(function, iterable)
# map takes function as first parameter and iterable as a second parameter
# It maps every element of the iterable to some other form
# The length of initial iterable and final result is same in map

data = [1, 2, 3, 4]
def cubed(elem):
    return elem ** 3

result = map(cubed, data)
print(result)  # <map_object> which is an iterator and can be looped. But to see its element we need
# to convert it to some other datatype
# print(list(result))

for each in list(result):
    print(each)



# filter()
# It also takes function and iterable as arguments
# It picks certain elements from the initial iterable
# But the size of initial iterable and final result may not be same in case of filter

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def get_even(elem):
    return elem % 2 == 0

result = filter(get_even, data)
print(result)  # <filter object>
print(list(result))  # [2, 4, 6, 8, 10]


# reduce()
# It also takes function and iterable as arguments
# It does operation based on the given function and return a single value
from functools import reduce

data = [1, 2, 3, 4, 5]
def add(x, y):
    return x + y

result = reduce(add, data)
print(result)  # 15

