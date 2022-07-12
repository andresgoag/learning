# for: execute a block of code for each element in iterable.
monday_temperatures = [9.1, 8.8, 7.6]

# Iterate over the indexes of iterable
for i in range(len(monday_temperatures)):
    print(monday_temperatures[i])

# Iterate over each element of iterable
for i in monday_temperatures:
    print(i)

for i in "banano":
    print(i)


# Dictionaries
student_grades = {"Mary": 9.1, "sim":8.8, "John":10}

# Over the keys
for name in student_grades:
    print(name)

# Or over the keys
for name in student_grades.keys():
    print(name)

# Over the values
for grade in student_grades.values():
    print(grade)

# Over elements tuple(key, value)
for i in student_grades.items():
    print(i)

# Assign each value of the tuple to a variable
for name, grade in student_grades.items():
    print(f"{name} tiene la nota de {grade}")

# With a list of tuples
people = [("bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, profession: {profession}")
