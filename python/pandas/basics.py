import pandas

'''
in pandas:
rows are named index
and columns, columns
'''



'''
Crear la siguiente matriz:

 2  4  6
10 20 30

'''

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])


'''
Comprobar tipo de un data frame: 
'''

type(df4)
dir(df4)



'''
Utilizando un metodo de un data frame
'''

df1.mean() # Retorna el promedio de cada index


'''
Anadir nombre a los index y columnas

'''

df3 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], index=["First", "Second"], columns=["Price", "Age", "Value"])




'''
Obtener un objeto pandas.Series a partir de una columna
'''

df3.Price



'''
Promedio de una serie
'''

df3.Price.mean()




'''
Crear la siguiente matriz con diccionarios

Jhon
Jack

'''

df4 = pandas.DataFrame([{"Name":"Jhon"}, {"Name":"Jack"}])




