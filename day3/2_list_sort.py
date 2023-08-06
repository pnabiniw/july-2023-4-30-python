# sort(reverse=True, key=function) method

a = [5, 3, 10, 1, 12, 2, 6]
a.sort()
print(a)  # [1, 2, 3, 5, 6, 10]

a.sort(reverse=True)
print(a)  # [10, 6, 5, 3, 2, 1]


a = [(5, 4), (3, 2), (4, 10), (12, 1), (1, 9)]
# output => [(12, 1), (3, 2), (5, 4), (1, 9), (4, 10)]


def get_second_num(data):
    return data[1]


a.sort(key=get_second_num)
print(a)


a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]

def get_last_num(data):
    return data[-1]


a.sort(key=get_last_num)
a.sort(key=get_last_num, reverse=True)
print(a)
