dir(str) # list the methods available for str

help(str.upper) # Help of the method upper of strings 

# Calling a method: use dot notation
x = "hello".upper()
y = "hello"
z = y.upper()

# Builtin python functions
dir(__builtins__)

# Custom help for a function
def foo():
    """Custom help text
    """
    return "hello"