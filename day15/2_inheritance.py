# Inheritance is the process of accessing the attributes in a Parent class by children classes
# Types of inheritance in Python
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# Single Inheritance
class A:
    a = 2


class B(A):
    pass


obj = B()
print(obj.a)  # 2


# Multiple Inheritance
class A:
    a = 3

class B:
    a = 5

class C(A, B):
    pass

obj = C()
print(obj.a)  # 3


# Multilevel Inheritance
class A:
    a = 5

class B(A):
    a = 10

class C(B):
    pass


# Hierarchical Inheritance
class A:
    a = 5

class B(A):
    pass

class C(A):
    pass


# Hybrid Inheritance
# It is the combination of multiple and hierarchical inheritance.

class A:
    a = 5

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(D):
    pass

obj = E()
print(obj.a)  # 4

print(E.mro())
# MRO => MRO stands for Method Resolution Order. It is the order in which attributes in an inheritance
# is accessed from the child class
