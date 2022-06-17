import mysql.connector

con = mysql.connector.connect(  #Credenciales para entrar a la base de datos
    user = "rocahost_kidsnew",
    password = '[0!42PpSDL',
    host = "70.32.23.55",
    database = "rocahost_kidsnew"
)


cursor = con.cursor()  #Crear un cursor para navegar la base de datos


#Traer todo de la base de datos
query = cursor.execute("SELECT * FROM wp5k_options") #SQL Statement para ejecutar, devolver todo de la tabla Dictionary
results = cursor.fetchall() #Devuelve una lista de tuplas con los valores retornados del query a la base de datos
print(results)
