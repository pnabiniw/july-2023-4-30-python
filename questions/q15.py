"""
What are classmethods and staticmethods in python?

"""
# instance method
# classmethod
# static method


class Student:
    def __init__(self, age):
        self.age = age

    @classmethod
    def age_from_birth_year(cls, year):
        age = 2023 - year
        return cls(age)  # Student(33)

    @staticmethod
    def grade():
        return "I study in grade 10"

s1 = Student(30)
s2 = Student.age_from_birth_year(1990)
print(s2.age)  # 33
