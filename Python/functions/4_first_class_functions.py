# First class objects in a language are handled uniformly throughout. 
# May be stored in data structures, passed as arguments, or used in control 
# structures. 

# A programming language is said to support first-class functions if it 
# treats functions as first-class objects. 
# Python supports the concept of First Class functions.



def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)

# Function as an argument
result = calculate(20, 4, operator=divide)



def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}.")



def get_friend_name(friend):
    return friend["name"]


friends = [
    {"name": "Rolf Smith","age": 24},
    {"name": "Adam Wool","age": 30},
    {"name": "Anne Pun","age": 27}
]


print(search(friends, "Rolf Smith", get_friend_name))

# as lambda
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
