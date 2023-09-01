# The classes which cannot be instantiated are called abstract classes
# This is created using "ABC" module from Python built-in

from abc import ABC, abstractmethod


class Animal(ABC):
    # This is an abstract class

    def sleep(self):
        print("I sleep at night")

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("I bark !!")


class Cow(Animal):
    def sound(self):
        print("I moo !!")


dog = Dog()
dog.sound()
dog.sleep()

cow = Cow()
cow.sound()
cow.sleep()
