# referencia para hacer string formatting de numeros https://blog.tecladocode.com/python-formatting-numbers-for-printing/

name = 'Andres'
last = 'Gomez'

message = "Hello %s %s!" % (name, last)

message2 = f"Hello {name} {last}!"

message3 = "Hi {}, with last name {}".format(name, last)