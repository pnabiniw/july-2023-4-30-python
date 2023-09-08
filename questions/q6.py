"""
1. How to swap two variables in python without using a third variable?
2. What will be the output of following code?
"""


names = ["Jon", "Jane", "Eren", "Ragnar", "Arya"]
print(list(enumerate(names)))

# [(0, "Jon"), (1, "Jane"), ]

for count, value in enumerate(names, start=1):
    print(count)
    print(value)

