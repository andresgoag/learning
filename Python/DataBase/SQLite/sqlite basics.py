import sqlite3


# 1. Connect to a database
conn = sqlite3.connect("lite.db") #Se pasa la direccion del archivo de la base de datos, si no existe, sera creado automaticamente.



# 2. Create a cursor object
cur = conn.cursor()



# 3. Write an SQL query

#Crear una tabla llamada store, con las columnas: "item" de tipo TEXT, "quantity" de tipo INTEGER y "price" de tipo flotante
create_table = "CREATE TABLE IF NOT EXISTS store (item  TEXT, quantity INTEGER, price REAL)" #SQL Statement as string
cur.execute(create_table)

#Adicionar 1 row a la base de datos:
item = ('Wine Glass', 8, 10.5)                     # Tupla con los datos a insertar, en el orden de las columnas de la tabla
insert_item = "INSERT INTO store VALUES (?,?,?)"   # SQL Statement, con ? en los valores a enviar
cur.execute(insert_item, item)                     # Aqui se reemplazaran los ? por los valores de la tupla


#Adicionar varias rows a la base de datos
items = [
    ('Watermelon', 25, 3.99),
    ('Coke', 12, 1.95)
]

cur.executemany(insert_item, items) #ejecutara el query por cada item en items




#Leer datos de la base de datos
select_query = "SELECT * FROM store"   # ej: SELECT id FROM store, devolvera los valores de id.     * selecciona todas las columnas
for row in cur.execute(select_query):    # Cuando se ejecuta un metodo execute con un select query, este puede ser tratado como un iterable, es una lista que cada item es una fila.
                                         # rows = cur.fetchall() -> Alternativamente se puede usar el metodo fetch all para crear la lista de las filas
    print(row)


# 4. Commit Changes
conn.commit()



# 5. Close Database connection
conn.close()
