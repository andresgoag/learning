# Create a new list applying a code with out the need of a for loop

temps = [221, 234, 340, 230]
new_temps = [temp/10 for temp in temps] # [code, for loop]
print(new_temps)

# with if statement
temps = [221, 234, 340, -9999, 230]
new_temps = [temp/10 for temp in temps if temp != -9999]
print(new_temps)

# if and else
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
