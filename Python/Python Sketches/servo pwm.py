import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(21,GPIO.OUT)    #Ponemos el pin 21 como salida
p = GPIO.PWM(21,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
p.start(7.5)               #Enviamos un pulso del 7.5% para centrar el servo
while True:
    
    p.ChangeDutyCycle(4)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda

GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script
