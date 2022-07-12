import mysql.connector

con = mysql.connector.connect(  #Credenciales para entrar a la base de datos
    user = "admin_cursoiot",
    password = "RouteUS-101",
    host = "pythonweb.tk",
    database = "admin_cursoiot"
)


cursor = con.cursor()  #Crear un cursor para navegar la base de datos


#Traer todo de la base de datos
query = cursor.execute("SELECT * FROM users") #SQL Statement para ejecutar, devolver todo de la tabla Dictionary
results = cursor.fetchall() #Devuelve una lista de tuplas con los valores retornados del query a la base de datos
print(results)
