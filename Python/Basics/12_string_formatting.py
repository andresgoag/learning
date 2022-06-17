# Referencias: Build 10 Real World Applications(Udemy)
# referencia para hacer string formatting de numeros https://blog.tecladocode.com/python-formatting-numbers-for-printing/

#Sirve para incluir el valor de una variable en una cadena para imprimir. "%s" caracter especial de python.

user_input = input("Enter your name: ")
message = "Hello %s!" % user_input
print(message)

#Otro metodo implementado a partir de python 6. Se requiere la f antes de abrir "".
message2 = f"Hello {user_input}!"
print (message2)


#Para insertar mas de un valor:
name = input("Enter your name: ")
surname = input("Enter your surname: ")

message = "Hello %s %s!" % (name, surname)
print(message)

message2 = f"Hello {name} {surname}!"
print (message2)

#Otra forma:
name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
