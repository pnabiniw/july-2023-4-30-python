class Department:
    def __init__(self, no_of_students):
        self.no_of_students = no_of_students

    def total_students(self, other):
        return self.no_of_students + other.no_of_students

    def __add__(self, other):
        return self.no_of_students + other.no_of_students


d1 = Department(10)
d2 = Department(25)
result = d1.total_students(d2)
print(result)  # 35

result = d1 + d2
print(result)  # 35

result = d1.__add__(d2)
