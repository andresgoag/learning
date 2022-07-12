# Python is a dynamically typed languaje, the data type of the variable is
# assigned by the data type of the value to assign.

#####################
# Simple Data Types #
#####################

# Integer
x = 10

# Float
z = 10.0  

# Get the data type
type(x)

# Math operators
math_ops = 1 + 3 * 4 / 2 - 7 ** 8

# Division "/" always returns a float
# Integer division, removes decinal (not rounded)
integer_division = 8 // 3

# Modulus
x = 13 % 3

# Addition assigment. Increment by
x += 1

# Substraction assigment
x -= 1

# Strings: use single and double quotes
y = "Hola"
d = 'Hola'

# Escape Character \: remove the syntactical meaning.
d = " el dijo \"Hola\" "

# Multiline string
multiline_string = '''
Esto es una cadena 

multiline
'''

'''Can be used to
long comments and
documentation'''

# Strings concatenation
greeting = "Hello"
name = "Andres"
complete = greeting + name











#######################
# Compound Data types #
#######################


# List
# can contain any type inside.
student_grades = [9.1, 8.8, 10]
mysum = sum(student_grades)
length = len(student_grades)
mean = mysum/length


# Tuples, inmutable and ordered.
monday_temperatures = (1, 4, 5)


# Sets, unordered, unchangeable, and do not allow duplicate values.
friends = {"anne", "bob", "Rolf"}
abroad = {"anne", "Rolf"}
others = {"Andres", "David", "Rolf"}

difference = friends.difference(abroad)
union = friends.union(others)
intersection = friends.intersection(others)

a = {1,2,3}
c = {1,2,3,4}

a.issubset(c) is True
c.issuperset(a) is True


#Dictionary, {Key:Value}
student_grades = {
    "Mary": 9.1, 
    "sim": 8.8, 
    "John": 10
}
mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum/length


# dictionary from string
import ast
ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")


# Bytes
# Bytes objects are a list of integers with values of [0, 256].
x = b"Hola"

# Bytes object, inmutable
b = bytes.fromhex("7E 00 0F 17 01 00 13 A2 00 41 04 6C 30 FF FE 02 49 53 B6")

# Bytearray object, mutable
D2_OFF = bytearray.fromhex(
    "7E 00 10 17 01 00 13 A2 00 41 04 6C 30 FF FE 02 44 32 04 D8")
