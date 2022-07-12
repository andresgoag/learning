import serial
import time


def crc_1(respuesta):
    crc = ord('\xFF')*256 + ord('\xFF')
    for i in range(len(respuesta)):
        crc = crc^ord(respuesta[i])
        for j in range(8):
            if crc%2 == 0:
                crc = crc/2
            else:
                crc = crc/2
                crc = crc^(ord('\xA0')*256+ord('\x01'))
    crc = hex(crc)
    crc = crc.split('x')[1]
    if len(crc)%2 != 0:
        crc = '0'+crc
    crc = crc.decode('hex')
    return crc







trama01 = '\x01\x01\x05\x00\x00\x06\xBC\xC4'

puerto = 'COM3'

#inicializacion del puerto serial 
ser = serial.Serial(
    port = puerto,                  #puerto de transmicion definido previamente
    parity = serial.PARITY_EVEN,    #paridad par
    bytesize = serial.EIGHTBITS,     #8 bits de datos
    stopbits = serial.STOPBITS_ONE,  # 1 bit de parada
    timeout = 0.1,                   #espera de 0.1 segundos
    xonxoff = 0,                    #control de flujao apagado
    rtscts = 0,                     #ready/clear to send apagado
    baudrate = 9600                 # velocidad en baudios 9600 
    )

if ser.is_open:
    ser.close()

ser.open()

ser.write(trama01)

respuesta = ''


x = ser.read()
if x == '\x01':
    print 'unidad correcta',x.encode('hex')
    respuesta = respuesta + x

    x = ser.read()
    if x == '\x01':
        print 'funcion correcta',x.encode('hex')
        respuesta = respuesta + x
        
        x = ser.read()
        print 'numero de bytes:',x.encode('hex')
        respuesta = respuesta + x

        
        x = ser.read()
        dato = bin(ord(x))
        dato = dato.split('b')[1]
        print 'Dato:', x.encode('hex')
        falta = 6-len(dato)
        dato = '0'*falta + dato
        for i in reversed(range(len(dato))):
            if dato[i] == '0':
                estado = 'bajo'
            elif dato[i] == '1':
                estado = 'alto'
            posicion = len(dato)-1-i
            print 'Salida',posicion,':',estado
        respuesta = respuesta + x


        a = ser.read()
        b = ser.read()
        crc_env = b+a
        crc_calc = crc_1(respuesta)
        if crc_env == crc_calc:
            respuesta = respuesta+a+b
            print 'crc:',crc_calc.encode('hex')


ser.close()

