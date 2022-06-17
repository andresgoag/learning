# Referencias: Build 10 Real World Applications(Udemy)

#Ejecutar una linea de codigo para toda la lista sin necesidad de hacer un for completo

temps = [221, 234, 340, 230] #Temperatures without decimal point
new_temps = [temp/10 for temp in temps] # [linea de codigo, condicion del for]
print(new_temps)

# list comprehension con condicional if
temps = [221, 234, 340, -9999, 230]
new_temps = [temp/10 for temp in temps if temp != -9999]
print(new_temps)

# list comprehension con condicional if and else
new_temps = [temp/10 if temp != -9999 else 0 for temp in temps]
print(new_temps)







# Dictionary comprehensions

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]


username_mapping = {user[1]: user for user in users}

#ejenplo log in
log = True

while log:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    try:
        _, username, password = username_mapping[username_input]
    except:
        print("Username not found!")
        continue

    if password_input == password:
        print("Your details are correct!")
        log = False
    else:
        print("Your details are incorrect!")
