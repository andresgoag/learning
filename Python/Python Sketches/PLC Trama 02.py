import serial
import time

trama02 = '\x01\x02\x04\x00\x00\x08\x78\xFC'

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

ser.write(trama02)

respuesta = ''


x = ser.read()
if x == '\x01':
    print 'unidad correcta',x.encode('hex')
    respuesta = respuesta + x

    x = ser.read()
    if x == '\x02':
        print 'funcion correcta',x.encode('hex')
        respuesta = respuesta + x
        
        x = ser.read()
        print 'numero de bytes:',x.encode('hex')
        respuesta = respuesta + x

        
        x = ser.read()
        dato = bin(ord(x))
        dato = dato.split('b')[1]
        print 'Dato:', x.encode('hex')
        falta = 8-len(dato)
        dato = '0'*falta + dato

        for i in reversed(range(len(dato))):
            if dato[i] == '0':
                estado = 'bajo'
            elif dato[i] == '1':
                estado = 'alto'
            posicion = len(dato)-1-i
            print 'Entrada',posicion,':',estado




        respuesta = respuesta + x

        x = ser.read(2)
        respuesta = respuesta + x
        crc = x
        print 'crc:',crc.encode('hex')


ser.close()

