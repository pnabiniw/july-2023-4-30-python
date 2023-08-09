# copy()
s1 = {1, 2, 3, 4, 5}
s2 = s1.copy()
print(s1)
print(s2)

# difference()
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8}
diff = s1.difference(s2)
print(diff)  # {1, 2, 3, 4}
diff = s1 - s2  # We can also use '-' operator for difference
print(diff)  # {1, 2, 3, 4}

# union()
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8}
result = s1.union(s2)
print(result)  # {1, 2, 3, 4, 5, 6, 7, 8}
result = s1 | s2
print(result)  # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection()
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8}
result = s1.intersection(s2)  # {5, 6}
print(result)
result = s1 & s2
print(result)  # {5, 6}

# isdisjoint()
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.isdisjoint(s2))  # False

# issubset
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8}
print(s2.issubset(s1))  # False
s3 = {4, 5, 6}
print(s3.issubset(s1))  # True
print(s1.issuperset(s3))  # True


# symmetric difference
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8}
result = s1.symmetric_difference(s2)
print(result)  # {1, 2, 3, 4, 7, 8}
result = s1 ^ s2
print(result)  # {1, 2, 3, 4, 7, 8}


# symmetric difference update
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8}
s1.symmetric_difference_update(s2)
print(s1)  # {1, 2, 3, 4, 7, 8}

