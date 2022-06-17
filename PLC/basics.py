import serial
import libscrc

ser = serial.Serial('COM9', timeout=0.3)

def modbusPLC(slave_address, function, starting_address, number_points):
    query = bytes.fromhex(slave_address + function + starting_address + number_points)
    crc16 = (libscrc.modbus(query)).to_bytes(2, byteorder='little')
    return query+crc16

def modbusSend(query):
    ser.reset_input_buffer()
    ser.write(query)
    response = ser.readline()

    pos = 0
    #Verificar slave_address
    if query[pos] == response[pos]:
        pos += 1
        #Verificar function
        if query[pos] == response[pos]:
            pos += 1
            #Tomar longitud e informacion
            bytes_num = response[pos]
            pos += 1
            data = response[pos:pos+bytes_num]
            pos += bytes_num
            #Chequear crc
            crc_recibido = response[pos:]
            crc_calculado  = libscrc.modbus(response[:-2]).to_bytes(2, byteorder='little')
            if crc_recibido == crc_calculado:
                return response, data, None
            else:
                return response, None, "crc, No coincide crc"
        else:
            return response, None, "byte[1], No coincide function"
    else:
        return response, None, "byte[0], No coincide slave_address"

    



#leer estado de salidas

estado_salidas = modbusPLC(slave_address = '01',
    function = '01',
    starting_address = '0500',
    number_points = '0006')

#leer estado de entradas
estado_entradas = modbusPLC(slave_address = '01',
    function = '02',
    starting_address = '0400',
    number_points = '0008')

# #leer registros
estado_registro = modbusPLC(
    slave_address = '01',
    function = '03',
    starting_address = '1456', # leer registro D1110, en decimal 1110 -1024, paso a hex + 1400
    number_points = '0001'
)

respuesta, datos, error = modbusSend(estado_salidas)
# respuesta, datos, error = modbusSend(estado_entradas)
# respuesta, datos, error = modbusSend(estado_registro)

if not error:
    print(respuesta.hex())
    print(datos.hex())
else:
    print(respuesta.hex())
    print(error)

# Convertir de Bytes a entero
# z = int.from_bytes(sample, 'big') #Convertir de bytes a entero. Sample es el objeto bytes a convertir, 'big' dice que el most significant byte es el primero, 'little' el most significant byte es el ultimo.
# print(z)

# Convertir de Enteros a Bytes
# number_bytes = 2
# b = (1024).to_bytes(number_bytes, byteorder='big') #Convertir 1024 a bytes. Especificar cuantos bytes, 'big' dice que el most significant byte es el primero, 'little' el most significant byte es el ultimo.
# print(b) #b'\x04\x00

ser.close()             # close port
