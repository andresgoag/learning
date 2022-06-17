# Built In Errors in Python

# IndexError
friends = ['Andres', 'David']
friends[2]  # becuase index 2 does not exists

# KeyError
movie = {
    "name": "Avengers",
    "year": 2020,
    "director": "Robert Patrick"
}
movie['release']  # because key release does not exists

# NameError
print(hello)  # because the variable hello has not been defined

# AttributeError
friends = ['Rolf', 'Jose', 'Charlie']
friends_nearby = ['Rolf', 'Anna']
# because a list has no attribute intersection. (sets do)
friends.intersection(friends_nearby)

# NotImplementedError


class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def login(self):
        raise NotImplementedError('This feature has not been implemented yet')

# RuntimeError
# An error that happens when running the program.
# Used to inherit other classes

# SyntaxError


class User  # missing colon.


def __init__(self, username, password) -> None:
    self.username = username
    self.password = password

# IndentationError


def sum(x, y):
    return x + y  # not using correct indentation

# TabError: When using tab insted of spaces. Always be consistent with spaces.


# TypeError: An operation with unsupported types
h = 5 + "s"

# ValueError
int('20.5')  # unsupported value as argument.

# ImportError: Raises when having a circular import

# DeprecationWarning: warning for a deprecation.
# Can be used for example in a method inside a class that is left for compatibility
# but has a better way of doing. raise DeprecationWarning('message')


# We always should create our own exception with better names


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0,")

    return dividend / divisor


grades = []

print("Welcome to the average grade program.")

try:
    average = divide(sum(grades)/len(grades))
except ZeroDivisionError as e:  # El tipo de error es opcional, se usa para tener varios except segun el error. "as e" se utiliza para guardar el error en una variable, e puede ser cualquier nombre de variable
    print("There are no grades yet in your list.")
except ValueError:
    print("Otro tipo de error")
else:
    # Solo se ejecuta si el try fue ejecutado exitosamente.
    print(f"The average grade is {average}")
finally:
    # Esta linea ocurre tanto si se ejecuto el try o si se ejecuto el except
    print("Thank you")


################################
###   Custom Error Classes   ###

# Declarar un custom error class, debe ser una subclase de un error ya existente para poder ser "raised"
class TooManyPagsReadError(ValueError):
    pass


class Book:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagsReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages.")
        self.pages_read += pages
        print(
            f"You have now read {self.pages_read} pages out of {self.page_count}.")


python101 = Book("Python 101", 50)
try:
    python101.read(35)
    python101.read(50)
except TooManyPagsReadError as e:
    print(e)













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
        # asegurarse que es instancia de Car
        if not isinstance(car, Car):
            raise (f'Tried to add a {car.__class__.__name__} to the garage, but can only add Car Types')
        self.cars.append(car)

        # To say the method is under construction insted of printing
        raise NotImplementedError("We can't add cars yet.")

    
ford = Garage()
ford.add_car('Fiesta')
print(len(ford))






# Custom errors

class MyCustomError(Exception):
    def __init__(self, message, code) -> None:
        self.code = code
        super().__init__(f'Error code {code}: {message}')


raise MyCustomError("An error happened", 500)





# Re raise errors

try:
    do_something("It is goingo to be an error")
except KeyError:
    print("Incorrecto values")
    raise
