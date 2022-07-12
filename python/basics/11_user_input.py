def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

# The input function, stops the execution of the program and waits for an
# input in the console. Returns a string.
user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))
