# Polymorphism in Python refers to many forms of the same functions or objects
# sum(), len(), max(), min() etc. they are some of the examples which follows polymorphism.
# These built-in functions can take different datatypes and performs their respective tasks

# There are two important aspects of Polymorphism:
# 1. Function / Method Overloading
# 2. Operator Overloading

# Function / Method Overloading

def addition(a, b):
    return a + b

def addition(a, b, c):
    return a + b + c

# result = addition(1, 2)   # It raises TypeError.
# print(result)
result = addition(1, 2, 3)
print(result)

# Though addition() is defined twice, only the latest definition is considered. So, Python doesn't support
# function overloading


# But we can give default argument so that we can pass both two and three arguments in the function call
def addition(a, b, c=0):
    return a + b + c

result = addition(1, 2)
print(result)  # 3
result = addition(1, 2, 3)
print(result)  # 6


class Employee:
    salary = 1200

    def description(self):
        return self.salary

    def description(self):
        return f"Salary is {self.salary}"


e = Employee()
print(e.description())   # The last definition is considered. So the result is "Salary is 1200"

