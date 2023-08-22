# Encapsulation is the process of data hiding in OOP approach of programming
# We can make the attributes private, public or protected.
# In Python, protected members can be created using a single underscore (_) and private members can
# be created using double underscore(__)


class Vehicle:
    _color = "blue"  # This is a protected property
    __mileage = 50  # This is a private property

    def __init__(self, doors, speed):
        self._doors = doors  # protected member
        self._speed = speed  # protected member

    def description(self):
        return f"color is {self._color}. Doors are {self._doors} and speed is {self._speed}"

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


v1 = Vehicle(4, 120)
print(v1._color)  # blue # Accessing protected member outside the class which is not recommended

v1.set_color("green")
print(v1.get_color())  # green


# Protected members of a class are meant to be used within a class or in their children class only.
# They are not meant to be used outside a class
# Python is not strict in OOP approach. So, it allows protected members to be accessed even outside
# the class. But, this is not recommended for developers as it doesn't follow proper convention.


# Private property is not accessible outside the class or in children classes
# print(v1.__mileage)   # It raises attribute error because __mileage is a private property
print(dir(v1))

print(v1._Vehicle__mileage)  # 50

# Though __mileage is a private property, we can access this property by _Vehicle__mileage. This
# is also called as "name mangling" in Python

