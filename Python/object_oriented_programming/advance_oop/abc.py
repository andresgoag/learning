# ABC examples
# ABCs let you define the functionallity without implementing it
# When a class has metaclass=ABCMeta, python doesn't let you instanciate it.
# you can't create an instance of animal.
# Also you cant instanciate from a class inherited from an ABC unless all
# abstract methods were overriden.

# ABC are useful: An stencil for the classes that will inherit from it. So be sure each subclass
# have the same methods and properties.

from abc import ABC, ABCMeta, abstractmethod

class Animalitos(ABC): ...
    # It is the same as defining the metaclass as below.

class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self): ...


class Dog(Animal):
    def __init__(self, name) -> None:
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name

    def num_legs(self):
        return 2