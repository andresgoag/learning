# While: Executes a block of code while a condition is true.

#print from 0 to 9
a = 0
while a < 10:
    print(a)
    a += 1

# Check user
username = ""
while username != "Andres":
    username = input("Enter your username: ")
print(f"Welcome, {username}")



# Loop and control (break and continue):
while True:
    username = input("Enter username: ")
    if username == "Andres":
        break # Ends loop execution.
    else:
        continue # Ends the current iteration and start the next one.

print(f"Welcome, {username}")
