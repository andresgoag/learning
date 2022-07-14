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

    # Assign value to a field with [key]=value notation
    def __setitem__(self, key,value):...

    # is used to show a string representation of your object to be 
    # read easily by others.
    def __str__(self):
        return f"Person {self.name}, {self.age} years old"

    #  Code oriented description: is used to show a string representation 
    # of the object. It is used by the debugger.
    def __repr__(self):
        return f"<Person('{self.name}',{self.age})>"


bob = Person("Bob", 35) #when a class is istanciated, __init__ is called
len(bob) # __len__
bob[0] # __getitem__
for car in bob:... # __getitem__
print(bob)  # __str__