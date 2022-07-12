# Every iterable in python has an index starting with 0.

#Syntax iterable_object[]

monday_temperatures = [9.1,8.8,"hola",7.5,5,6]

print(monday_temperatures[1]) # 8.8
print(monday_temperatures[1:3]) # [8.8, 7.5]
print(monday_temperatures[1:]) # from index 1 to last
print(monday_temperatures[:2]) # from start to index n-1
print(monday_temperatures[-1]) # last item
print(monday_temperatures[-2:]) # last 2 items

print(monday_temperatures[2][3]) # 4th element of the 3rd element

#Dictionary index are the "keys". Dictionaries are unordered
student_grades = {"Mary": 9.1, "sim":8.8, "John":7.5}
print(student_grades["Mary"]) # 9.1
