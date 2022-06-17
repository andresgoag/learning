# Referencias: Build 10 Real World Applications(Udemy)

#for loop sirve para ejecutar una porcion de codigo por cada elemento de un objeto
monday_temperatures = [9.1, 8.8, 7.6]

#Se puede crear una lista segun la longitud del objeto e iterar a traves de ella:
for i in range(len(monday_temperatures)):
    print(monday_temperatures[i])

#Se puede iterar sobre cada elemento del objeto iterable
for i in monday_temperatures:
    print(i)

for i in "banano":
    print(i)


# Se puede usar for con diccionarios tambien:
student_grades = {"Mary": 9.1, "sim":8.8, "John":10}
#Itera en los keys:
for name in student_grades:
    print(name)

#Se puede escoger sobre que se va a iterar:
for name in student_grades.keys():
    print(name)

for grade in student_grades.values():
    print(grade)

for i in student_grades.items():
    print(i) #Retornara el par Key:Value como una tupla (Key, Value).


# Se puede iterar con dos o mas variables al mismo tiempo:

#Con un diccionario
for name, grade in student_grades.items():
    print("{} tiene la nota de {}".format(name,grade))


#Con una lista de tuplas
people = [("bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, profession: {profession}")
