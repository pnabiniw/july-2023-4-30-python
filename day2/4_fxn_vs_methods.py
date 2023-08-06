def addition(a, b):
    print(a + b)

result = addition(2, 3)
print(result)
# Here addition() is a user-defined function
# There are several built-in functions len(), print(), map(), reduce(), filter(), sum()


class Student:
    def age_after_ten_years(self, current_age):
        return current_age + 10


student1 = Student()
age_after_ten_years = student1.age_after_ten_years(10)
print(age_after_ten_years)

# Here age_after_ten_years() is a method of class Student which can be called using student
# object only
