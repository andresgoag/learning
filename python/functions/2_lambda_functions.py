# Lambda Functions


# nomral function
def add(x,y):
    return x + y

#as a lambda
add = lambda x, y: x + y


# Common uses: comprehensions and when a callable is needed.

# normal function
def double(x):
    return x * 2
sequence = [1,3,5,9]

# list comprehension
doubled = [double(x) for x in sequence]

# with map and list
doubled = list(map(double, sequence))

# with lambda
doubled = [(lambda x: x*2)(x) for x in sequence]

doubled = list(map(lambda x: x*2, sequence))