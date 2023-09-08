"""
1. What is the order of the arguments in functions and methods
a. Keyword Args / Default Args 2
b. Positional 1
c. **kwargs 4
d. *args 3

2. Explain *args and **kwargs
"""

def addition(*args, **kwargs):
    print(args)  # (2, 3, 4, 5)
    print(kwargs) # {"a": 8, "b": 10}


addition(2, 3, 4, 5, a=8, b=10)
