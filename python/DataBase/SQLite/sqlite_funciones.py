import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item  TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price)) #Los > seran reemplazados por las variables en el segundo parentesis, en el orden
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall() # Devuelve una lista y cada item es una fila
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,)) #Se requiere la ultima coma del segundo parentesis, solo cuando hay un solo parametro
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price =? WHERE item =?", (quantity, price, item)) #Actualizar el valor de la columna quantity y price de la fila con item especificado
    conn.commit()
    conn.close()





insert("Water Glass", 20, 3)
print(view())
item_to_delete = "Water Glass"
delete(item_to_delete)
print(view())
update(80,90,"Wine Glass")
print(view())
