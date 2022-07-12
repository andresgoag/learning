# Functions that call it selfs. must be carefull with infinite loop.

def factorial(n):
    if n==1:
        return 1
    
    return n * factorial(n - 1)


print(factorial(10))