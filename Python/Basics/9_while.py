# Referencias: Build 10 Real World Applications(Udemy)


#Es un loop que se ejecuta siempre que (while) se cumpla una condicion

#Imprimir los numeros del 0 al 9:
a = 0
while a<10:
    print(a)
    a = a+1

#Comprobar un usuario:
username = ""

while username != "Andres":
    username = input("Enter your username: ")

print(f"Welcome, {username}")
print("Welcome, {}".format(username))



#Controles del loop (break and continue):

while True:
    username = input("Enter username: ")
    if username == "Andres":
        break #Termina la ejecucion del loop y lleva el control flow a la linea siguiente despues del loop.
    else:
        continue #Ignora el resto del codigo del bloque del loop y continua con la siguiente iteracion.

print(f"Welcome, {username}")
