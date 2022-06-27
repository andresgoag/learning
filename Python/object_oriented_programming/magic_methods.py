# Methods with __ at both sides. Will be called by special syntax of python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars = []

    # Defines how the len of the object will be determined.
    def __len__(self):
        return len(self.cars)

    # Defines which item return when the index operator is used.
    # If __getitem__ is define, the instance can be used as an iterable.
    def __getitem__(self, i):
        return self.cars[i]

    # Useful representation of the object.
    def __str__(self):
        return f"Person {self.name}, {self.age} years old"

    #  Code oriented description
    def __repr__(self):
        # Esta funcion se utiliza en el python debugger,
        # sirve para dar una pista de como reconstruir el objeto facilmente
        # Retorna un string que representa el objeto
        return f"<Person('{self.name}',{self.age})>"



bob = Person("Bob", 35) #when a class is istanciated, __init__ is called
len(bob) # __len__
bob[0] # __getitem__
for car in bob:... # __getitem__
print(bob)  # __str__