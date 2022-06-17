import serial



ser = serial.Serial('COM4', timeout=0.1)  # open serial port



#Cambiar el estado de una salida digital remota
D2_ON = "7E 00 10 17 01 00 13 A2 00 41 04 6C 30 FF FE 02 44 32 05 D7"
D2_OFF = "7E 00 10 17 01 00 13 A2 00 41 04 6C 30 FF FE 02 44 32 04 D8"



D2_ON = bytes.fromhex(D2_ON) #Crea un objeto bytes
D2_OFF = bytearray.fromhex(D2_OFF) #Crea un objeto bytearray


while True:
    x = input()
    if x == "ON":
        ser.write(D2_ON)
    elif x == "OFF":
        ser.write(D2_OFF)
    elif x == "terminar":
        break
    else:
        print("Escriba on o off")





#Muestra del estado de entradas

query_puertos = bytes.fromhex("7E 00 0F 17 01 00 13 A2 00 41 04 6C 30 FF FE 02 49 53 B6")

ser.reset_input_buffer() #Limpiar el bufer para preparar la llegada de la trama de query de entradas. Esto sirve para usar el readline()
ser.write(query_puertos)

x = ser.readline() #Devuelve un objeto bytes, si se imprime se muestra como ASCII

y = x.hex() #Para crear un string para visualizar los bytes como hexadecimal
print(y)

sample = x[-2:] #Para interpretar los datos de lo que se lee en el puerto simplemente se usa el slice operator, ya que el objeto bytes es una lista de enteros "0 <= x < 256". Esta operacion retorna un entero
print(sample)



#COnvertir de Bytes a entero
z = int.from_bytes(sample, 'big') #Convertir de bytes a entero. Sample es el objeto bytes a convertir, 'big' dice que el most significant byte es el primero, 'little' el most significant byte es el ultimo.
print(z)



#Convertir de Enteros a Bytes
number_bytes = 2
b = (1024).to_bytes(number_bytes, byteorder='big') #Convertir 1024 a bytes. Especificar cuantos bytes, 'big' dice que el most significant byte es el primero, 'little' el most significant byte es el ultimo.
print(b) #b'\x04\x00







ser.close()             # close port
