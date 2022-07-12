import serial
import time




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

while True:
    x = raw_input(':')
    ser.write(x)

ser.close()

