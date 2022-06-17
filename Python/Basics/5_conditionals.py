# Referencias: Build 10 Real World Applications(Udemy)

# Para usar condicionales:
#if: evaluar una condicion y ejecutar el codigio si la condicion se cumple.
#if y else: cuando se quiere ejecutar una porcion del codigo si la condicion es verdadera y ejecutar otra porcion de codigo si la condicion es falsa.
#NOTA: else siempre debe ir en la parte final del condicional.

#Curiosidad, para comparar tipos de data, se puede utilzar "isinstance(obj, type)"" esta funcion devuelve verdadero si "obj" es type "type"



# Comparisons: ==, !=, >, <, >=, <=


def mean (value):
    if type(value) == dict: # tambien puede ser if isinstance(values, dict)
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean

x = [1,2,3,4,5,6,7,8,9]
print(mean(x))

student_grades = {"Mary": 9.1, "sim":8.8, "John":10}
print(mean(student_grades))


#Cuando se quiere comprobar varias condiciones se puede agregar elif cuantas veces sea necesario.
x = 3
y = 1
if x > y:
    print("x is greater than y")
elif x == y:
    print("x equals to y")
else:
    print("x is less than y")


#Si se quiere comprobar dos condiciones:
x = 1
y = 1

if x == 1 and y==1:
    print("Yes")
else:
    print("No")


#Si se quiere comparar uno u otro condicional
x = 1
y = 1

if x == 1 or y==2:
    print("Yes")
else:
    print("No")
