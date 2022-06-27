# Use "def" keyword to create a function. same naming rules as variable follow by (arguments).
# The function must be created before calling it.

def mean (mylist):
    """Doc string: to create the help of the function.
    """
    the_mean = sum(mylist)/len(mylist)
    return the_mean

x = [1,2,3,4,5,6,7,8,9]
mean_x = mean(x)


# Local and global variable
# Global: general context of the program.
d = "hello"
def context_example():
    # Local: Created inside a function. Only exists inside the function
    x = 5
    # global keyword: reference to the global variable.
    global d
    print(d)
context_example()


# Passing arguments to the function
# arguments with no default value first than the ones with default value.
def rectangle_area(a,b=5):
    return a * b

print(rectangle_area(2)) # 2 will be the value for a. b will use its default value.
print(rectangle_area(2,3)) # Values assigned in order
print(rectangle_area(b=3, a=2)) # With keyword arguments order does not matter.




#Functions with an indefinite number of Non-keyword Arguments
def mean (*args):
    # args will be a tuple with all the values passed
    return sum(args)/len(args)


def add(x, y):
    return x + y

nums = [3, 5] # A list with the same number of arguments
add(*nums) # destructure the list to be arguments




#Functions with an indefinite number of keyword Arguments
def mean_kw(**kwargs): 
    # kwargs will be a dictionary with all the keyword arguments.
    return kwargs

print(mean_kw(a=1, b=2, c=3))



def add(x, y):
    return x + y

nums = {"x": 3, "y": 5} # a dict with its keys named the same as the parameters of the function.
add(**nums)