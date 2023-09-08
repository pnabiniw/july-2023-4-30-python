"""
Explain method overloading and overriding in python
"""
class A:
    def description(self):
        return "Hello"


class B(A):
    def description(self):
        return "World"

    def description(self):
        return "Python"


def addition(a, b, c=0):
    return a + b + c

addition(2, 3)
addition(1, 2, 3)