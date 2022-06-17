import psycopg2
import os

URL = os.environ.get('DATABASE_URL')

def create_table():
    conn = psycopg2.connect(f"dbname='database1' user='postgres' password='RouteUS-101' host='{URL}' port='5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item  TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()




create_table()
