# Referencias: Build 10 Real World Applications(Udemy)


#Reading a file
myfile = open("fruits.txt") #Crea un "file object"
#Cursor concept: cuando se abre un archivo, el cursor se encuentra en la posicion incial, al aplicar el metodo read(), el cursor se desplaza hasta la ultima posicion del archivo. Por lo cual si se aplica nuevamente el metodo read() no devolvera nada.
#Guardar el contenido del archivo en una variable. y esta varible puede er utilizada cuantas veces sea necesario.
content = myfile.read()
#Es buena practica cerrar el "file object" una vez finalice el procesamiento del "file object"
myfile.close()
print(content)



#Better practice: usando "with"
#Todo el codigo relacionado con el procesamiento del archivo debe ser indentado dentro del with
with open("fruits.txt") as myfile:
    new_content = myfile.read()
#Cuando el codigo dentro del with finalice, se aplicara el metodo close automaticamente.
print(new_content)


#Para url diferentes:
url = "new_folder/fruits.txt" #Se debe escribir la direccion relativa del archivo a la carpeta en la cual esta el script de python.




#Write in a file:
#NOTA: Si se utiliza la direccion de un archivo que ya existe, este metodo sobreescribira todo el contenido del mismo.
with open("vegetables.txt", "w") as myfile: #Modos de la funcion open: r (read), w (write), a(append)
    myfile.write("Tomato")

#Adicionar lineas a un archivo existente:
with open("vegetables.txt", "a") as myfile: #El modo append no permite leer el contenido del archivo
    myfile.write("\nNew Line")


#Modo que permite leer y escribir al mismo tiempo: a+
with open("vegetables.txt", "a+") as myfile:
    myfile.write("\nNew Line") #Al agregar esta linea, el cursor se desplaza hasta el final del archivo
    myfile.seek(0) #Para regresar el cursor a la posicion inicial
    content = myfile.read()

print(content)
