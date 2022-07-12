# ABCs let you define the functionallity without implementing it.
# ABCs are useful as an stencil for the classes that will inherit from it. 
# ABCs can't be instanciated unless all abstract methods are overriden.

from abc import ABC, ABCMeta, abstractmethod

# define the class to be an abstract class with (metaclass=ABCMeta) or 
# inherited from ABC class

class Animalitos(ABC): ...

class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    # define an abstract method
    @abstractmethod
    def num_legs(self): ...

# must override the abstact method to be a subclass of animal
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