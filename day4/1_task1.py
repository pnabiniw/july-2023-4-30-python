# Create a list of first 10 multiples of 3 using list comprehension

a = []
for value in range(1, 11):  # 1, 2
    a.append(value * 3)  # [3, 6, 9, 12...., 30]

print(a)

# Using Comprehension
a = [i * 3 for i in range(1, 11)]
print(a)
