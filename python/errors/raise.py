# Raising errors

class Car:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self) -> None:
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            # raise the error
            raise (f'Tried to add a {car.__class__.__name__} to the garage, but can only add Car Types')
        self.cars.append(car)




# In case you want to do something in the except clause and reraise the error so
# it can spread, you can use the raise keyword.

try:
    x = 0/0
except ZeroDivisionError:
    print("Incorrect values")
    raise
