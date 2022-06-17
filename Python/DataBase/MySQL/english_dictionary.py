import mysql.connector

con = mysql.connector.connect(  #Credenciales para entrar a la base de datos
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)


cursor = con.cursor()  #Crear un cursor para navegar la base de datos


#Traer todo de la base de datos
query = cursor.execute("SELECT * FROM Dictionary") #SQL Statement para ejecutar, devolver todo de la tabla Dictionary
results = cursor.fetchall() #Devuelve una lista de tuplas con los valores retornados del query a la base de datos
print(results[0])



#Ejemplo para obtener de la base de datos algo especifico
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'inlay' ") #devolver la entrada de la tabla Dictionary que en el campo Expression tenga inlay
results = cursor.fetchall() #Devuelve una lista de tuplas con los valores retornados del query a la base de datos
print(results)




#Ejemplo con una palabra que tiene multiples significados, es decir en el campo expression esta varias veces.
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'line' ")
results = cursor.fetchall()

definiciones = "Las definiciones para la palabra son:\n"
for result in results:
    definicion = result[1]
    definiciones = f"{definiciones}{definicion}\n"

print(definiciones)






#Ejemplo con una entrada que no existe
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'asdfg' ")
results = cursor.fetchall() #Si la palabra existe, se obtiene una lista de tuplas con los resultados, si la palabra no existe se obtiene una lista vacia

print(results) #Esta lista esta vacia

if results: #Si una lista esta vacia, significa False
    for result in results:
        print(result[1])
else:
    print("no word found")
