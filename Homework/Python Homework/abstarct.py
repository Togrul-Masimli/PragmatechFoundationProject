from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeNoice(self):
        pass


class Employee(ABC):
    @abstractmethod
    def montlySalary(self,weaklyhours,hourlypay):
        pass


class Programmer(Employee):
    def montlySalary(self, weaklyhours, hourlypay):
        return weaklyhours * hourlypay

class Dog(Animal):
    def makeNoice(self):
        print("Hav")

class Cat(Animal):
    def makeNoice(self):
        print("Meow")

class Cow(Animal):
    def makeNoice(self):
        print("Mo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.makeNoice()
cat.makeNoice()
cow.makeNoice()

prg1 = Programmer()
print(prg1.montlySalary(40,15))