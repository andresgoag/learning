import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout = 1)
ser.open()


while True:
    ser.write('hola')
    x = ser.readline()
    print x
ser.close()
