# First Class Functions

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide) # Se pasa como keyword argument la funcion que se desea ejecutar al ejecutar la funcion calculate
print(result)







#Ejemplo 2 First Class Functions

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

print(search(friends, "Rolf Smith", lambda friend: friend["name"])) #Se puede escribir como un lambda function y no se tendria que declarar la funcion get_friend_name
