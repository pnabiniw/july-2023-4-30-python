# Class methods are the methods which takes class as the first parameter rather than self
# Class method is created using @classmethod decorator
# Static methods are the methods which neither takes class nor self as a parameter. They are like
# a normal function which doesn't change the state of the class.
# Static method is created using @staticmethod decorator


class Student:
    def __init__(self, age):
        self.age = age

    @classmethod
    def from_birth_year(cls, year):
        age = 2023 - year
        return cls(age)

    @staticmethod
    def institution_name():
        return "Broadway"


s1 = Student(25)
print(s1.age)  # 25
s2 = Student.from_birth_year(1992)
print(s2.age)  # 31

print(s2.institution_name())  # Broadway

# Here "from_birth_year" method is a class method. And it is also sometimes termed as a "factory method"
