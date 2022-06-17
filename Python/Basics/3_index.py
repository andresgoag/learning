# Referencias: Build 10 Real World Applications(Udemy)

#todos los objetos iterables en python tienen un "index" empezando en 0

#Operador []
monday_temperatures = [9.1,8.8,"hola",7.5,5,6]

print(monday_temperatures[1]) #Imprime 8.8
print(monday_temperatures[1:3]) #Nueva lista [8.8, 7.5]
print(monday_temperatures[1:]) #Desde index 1 hasta el final
print(monday_temperatures[:2]) #Desde el inicio hasta la posicion n-1
print(monday_temperatures[-1]) #El ultimo elemento
print(monday_temperatures[-2:]) #Los ultimos dos items


#Index compuesto
print(monday_temperatures[2][3]) #imprime el 4er elemento del 3er elemento de monday_temperatures


#El index de los diccionarios son sus "Key", por lo tanto estos no tienen un orden definido
student_grades = {"Mary": 9.1, "sim":8.8, "John":7.5}
print(student_grades["Mary"]) #Imprime el value del key asignado
