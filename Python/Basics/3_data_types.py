# Referencias: Build 10 Real World Applications(Udemy) /// Zenva - Learn python from making a game

# la declaracion de variables en python se da dependiendo del valor que se le asigne a la variables


# Simple data types
import ast
x = 10  # Integer
z = 10.0  # Float

print(type(x))  # conocer el tipo de dato

# Operaciones con numeros
math_ops = 1 + 3 * 4 / 2 - 7 ** 8
# la division siempre retorna un float
# para dejar un integer en division
integer_division = 8 // 3  # no redondea, solo quita el decimal

# Modulus
x = 13 % 3

# El operador += incrementara el valor de la variable de la izquiera el valor de la variable de la derecha.
x += 1


# strings
y = "Hola"  # String
d = 'Hola'

# se puede usar " dentro de un string declarado con "".
# Pero se debe poner un backslash antes de las comillas texto \"
# Esto se llama escaping: putting a backslash in front of a character to remove meaning.

d = " el dijo \"Hola\" "

multiline_string = '''
Esto es una cadena 

multiline
'''

'''Pueden servir
para escribir un comentario
muy largo'''

# Concatenar strings
greeting = "Hello"
name = "Andres"
complete = greeting + name
print(complete)


# Compound Data types


# List, una lista puede contener cualquier dato
student_grades = [9.1, 8.8, 10]
# Example using python built in functions
mysum = sum(student_grades)
length = len(student_grades)
mean = mysum/length
print(mean)


# Tuples, no son mutables
monday_temperatures = (1, 4, 5)


# Sets
friends = {"anne", "bob", "Rolf"}
abroad = {"anne", "Rolf"}
others = {"Andres", "David", "Rolf"}

difference = friends.difference(abroad)
print(difference)
union = friends.union(others)
print(union)
intersection = friends.intersection(others)
print(intersection)


#Dictionary, {Key:Value}
student_grades = {"Mary": 9.1, "sim": 8.8, "John": 10}
mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum/length
print(mean)

# dictionary from string
ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")


# Bytes Objects, si se imprime se muestra como ASCII
x = b"Hola"
# Un bytes o bytearray object es una lista de enteros entre "0 <= x < 256" que representan los bytes. los bytes no son mutables, los bytearray son mutables
# Crea un objeto bytes
b = bytes.fromhex("7E 00 0F 17 01 00 13 A2 00 41 04 6C 30 FF FE 02 49 53 B6")
# Crea un objeto bytearray
D2_OFF = bytearray.fromhex(
    "7E 00 10 17 01 00 13 A2 00 41 04 6C 30 FF FE 02 44 32 04 D8")
