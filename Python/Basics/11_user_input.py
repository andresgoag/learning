# Referencias: Build 10 Real World Applications(Udemy)

def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"


#Todo lo que retorna la funcion input es un "str" por lo cual el dato se debe convertir a la instancia deseada.
user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))
