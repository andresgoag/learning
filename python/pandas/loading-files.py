import os

os.listdir() # Devuelve una lista de archivos en la carpeta


import pandas

df1 = pandas.read_csv("supermarkets/supermarkets.csv")
df2 = pandas.read_json("supermarkets/supermarkets.json")
df3 = pandas.read_excel("supermarkets/supermarkets.xlsx", sheet_name="nombre", engine='openpyxl') # sheet name puede ser string o int empezando de 0.
df4 = pandas.read_csv("supermarkets/supermarkets-commas.txt")
df5 = pandas.read_csv("supermarkets/supermarkets-semi-colons.txt", sep=';')



'''
Especificar el header de un data frame
'''
df6 = pandas.read_csv("supermarkets/supermarkets-commas.txt", header=None) # sin headers, le asigna numeros


'''
Darle nombres a las columnas
'''
df6.columns = ['ID', 'Address', 'City', 'ZIP', 'Country', 'Name', 'Employees']



'''
change index column
'''
new_frame = df5.set_index('ID') # pone que la columna id, sea el id
df5.set_index('ID', inplace=True, drop=False) # modifica permanentemente el df5, drop=False, previene que la columna original no se pierda


'''
Label based index: acceder a porciones de datos. upper bound inclusive
'''

df5.loc["primer": "tercer", "City":"ID"] # especificar el rango de index (tener una columna set as index) y el rango de columns

df5.loc[1, "City"] # un unico valor


'''
index based index: upper bound exclusive (normal python)
'''

df5.iloc[1:3, 1:3]


'''
Get series of rows/columns
devuelve una serie de los index o columns
'''

df5.index

df5.columns


'''
Eliminar filas/columnas 
'''

# 0 row, 1 column

df5.drop["city", 1] # index, row/column

df5.drop(df5.index[0:3], 0) # eliminar filas desde la 0 hasta la 2

df5.drop(df5.columns[0:3], 1) # eliminar columnas desde la 0 hasta la 2




'''
update and add rows and columns
'''

len(df5.index)

#se debe pasar una lista con el numero de elementos en las filas o columnas

df5.shape # devuelve una tupla (cantidad de filas, cantidad de columnas)

# para llenar con un unico valor:
df5['Continent'] = df5.shape[0]*['North America']



df7["Continent"] = df7["Country"] + ', ' + "North America"


para añadir una fila, se traspone la tabla, se añade una columna y se vuelve a trasponer

df5_t = df7.T
df5_t["My address"] = ["City", "Country", 10, 7, "shop", "state", "continente"]

df5 = df5_t.T


