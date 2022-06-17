# Lambda Functions


#Sintaxis normal de una funcion
def add(x,y):
    return x + y

print(add(5,7))





#Reescrita como lambda Functions
print((lambda x, y: x + y)(5,7))

#asignandole un nombre para que pueda ser reutilizada
add = lambda x, y: x + y
print(add(5,7))





#Casos de uso comun de las lambda Functions:

#1. doblar una lista usando list comprehension
def double(x):
    return x * 2

sequence = [1,3,5,9]
doubled = [double(x) for x in sequence]
print(doubled)
doubled = list(map(double, sequence)) #hace lo mismo que list comprehension
print(doubled)

#Reescrita con lambda Functions
doubled = [(lambda x: x*2)(x) for x in sequence]
print(doubled)
doubled = list(map(lambda x: x*2, sequence))
print(doubled)
