# Referencias: Build 10 Real World Applications(Udemy)

#Conceptos: Un modulo tiene metodos. ej: time es el modulo, sleep es un metodo de time


#Built-in modules
#Escritos en C originalmente con python interpreter
import sys #se puede utilizar el comando "sys.builtin_module_names", para tener una lista de los builtin modules de python.
import time #Para usar uno de los modulos de sys, se debe importar, se puede usar "dir(time)" para conocer que metodos tiene el modulo, Se puede usar help. ej> "help(time.sleep)" para ver la ayuda.
time.sleep(10) #Detiene la ejecucion del script durante 10 segundos.


#Standard  modules.
#Escritos en python y estan albergados en la carpeta Lib de la instalacion de python. tambien se puede utilizar las funciones dir() y help()
import os
if os.path.exists("original.csv"):
    print("Existe")
else:
    print("no existe")


#Third Party modules
#Escritos por otras personas, se deben instalar, frecuentemente se usa "pip" en el command line para instalar libreiras de terceros.
import pandas

while True:
    if os.path.exists("original.csv"):
        data = pandas.read_csv("original.csv")
        print(data.mean()["st1"])
    time.sleep(5)
