# IndexError
friends = ['Andres', 'David']
friends[2]  # becuase index 2 does not exists.




# KeyError
movie = {
    "name": "Avengers",
    "year": 2020,
    "director": "Robert Patrick"
}
movie['release']  # because key release does not exists.




# NameError
print(hello)  # because the variable hello has not been defined.




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




# RuntimeError: An error that happens when running the program.
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