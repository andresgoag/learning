import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='RouteUS-101' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item  TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='RouteUS-101' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price)) #Los > seran reemplazados por las variables en el segundo parentesis, en el orden
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='RouteUS-101' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='RouteUS-101' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,)) #Se requiere la ultima coma del segundo parentesis, solo cuando hay un solo parametro
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='RouteUS-101' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price =%s WHERE item =%s", (quantity, price, item)) #Actualizar el valor de la columna quantity y price de la fila con item especificado
    conn.commit()
    conn.close()


#create_table()
insert("Agua",10,3)
print(view())
delete("Agua")
print(view())
update(66,6,"Orange")
print(view())
