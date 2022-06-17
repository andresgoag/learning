# Referencias: Build 10 Real World Applications(Udemy) /// Zenva - Learn python from making a game

#Para crear una funcion se utiliza el comando "def", se nombra con las mismas reglas que las variables y entre parentesis se puede pasar argumentos.
#La funcion debe ser creada antes de ser utilizada.

def mean (mylist):
    """ 
    Con triple " se declara el "doc string", esta cadena la mostrara python cuando se busque 
    esta funcion en la ayuda help(mean)
    Aqui se debe especificar brevemente, que hace la funcion, cuales y de que tipo son los
    parametros que recibe y cual es el valor que retorna.
    """

    the_mean = sum(mylist)/len(mylist)
    return the_mean

x = [1,2,3,4,5,6,7,8,9]
mean_x = mean(x)
print(mean_x)



#Concepto variable local y global:

d = "hola" #Si la variable existe en el contexto general del programa (fuera de la funcion) se llama Global Variable

def ejemplo_global():
    x = 5 #Las variables que existen dentro de la funcion se llaman Local Variable, ya que solo existen dentro de la funcion
    global d # Con "global" se declara una referencia dentro de la funcion a la variable global.
    print(d)

ejemplo_global() # Este programa imprimira el valor global de la variable d




#Para funciones con varios parametros hay varias opciones para llamarla:
def rectangle_area(a,b=5): #Un parametro puede tener un "Default value"
    return a * b

print(rectangle_area(2)) # 2 sera el valor de a, y b utilizara su "Default value"
print(rectangle_area(2,3)) #Se asigna los argumentos a los parametros en orden: a=2 y b=3 (Se cambia el "Default value" a b)
print(rectangle_area(b=3, a=2)) #Cuando se usa "Keyword arguments" el orden no importa, se asigna al parametro indicado

#los parametros que tendran "Default value" deben ser declarados despues de los parametros "Non Default values"
#def area (a=4, b) No se puede utilizar



#Functions with an indefinite number of Non-keyword Arguments
def mean (*args): #Se define que sera una cantidad indefinida de non keywords arguments con "*", puede llevar cualquier nombre, por convencion se usa la palabra args. Esto generara una tupla que continene todos los argumentos.
    return sum(args)/len(args)

print(mean(1,2,3,4,5,6,7,8,9))



def add(x, y):
    return x + y

nums = [3, 5] #La lista debe contener el mismo numero de items que de argumentos.
add(*nums) #Esto deconstruira la variable nums para pasar como argumentos x=3 y y=5




#Functions with an indefinite number of keyword Arguments
def mean_kw(**kwargs): #Se define que sera una cantidad indefinida de keywords arguments con "**", puede llevar cualquier nombre, por convencion se usa la palabra kwargs. Esto generara un diccionario que continene todos los key word arguments.
    return kwargs

print(mean_kw(a=1, b=2, c=3))




def add(x, y):
    return x + y

nums = {"x"=3, "y"=5} si se tiene un diccionario, en el cual los key corresponden al nombre de los argumentos de la funcion, se pueden pasar como named arguments
add(**nums)






# Funciones recursivas
# ej: factorial

# Las funciones recursivas deben tener una solucion, sino se entra en un loop infinito.


def factorial(n):
    if n==1:
        return 1
    
    return n * factorial(n - 1)


print(factorial(10))
