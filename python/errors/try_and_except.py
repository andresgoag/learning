# Catch exceptions with try and except

# function that raises an error somewhere.
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0,")

    return dividend / divisor


grades = [1,2,0]

# This block will always be executed
try:
    average = divide(sum(grades)/len(grades))

# If the try block raises an error, can be catched with an except block
# You can specify the type of error that will execute the except block
# the error can be saved to a variable to have access to it.
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")

except ValueError:
    print("Otro tipo de error")

# The else clause will be executed if the try block was executed sucessfully
else:
    print(f"The average grade is {average}")

# The finally clause will always be executed no matter if the try succed or not.
# after the try and exept blocks are executed.
finally:
    print("Thank you")
