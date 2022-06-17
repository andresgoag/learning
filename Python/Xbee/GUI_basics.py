from tkinter import *

from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.io import IOLine, IOMode, IOValue, IOSample



BAUD_RATE = 9600
coordinador = None
router1 = None
DIO2_indicator = True
analog_reading = None
digital_reading = None



window = Tk()


def open_device():
    global coordinador
    global router1
    global window

    PORT = e1_value.get()
    coordinador = XBeeDevice(PORT, BAUD_RATE)
    router1 = RemoteXBeeDevice(coordinador, XBee64BitAddress.from_hex_string("0013A20041046C30"))
    coordinador.open()
    window.after(500, read_values)


def close_device():
    global coordinador
    coordinador.close()


def led_status():
    global DIO2_indicator
    global router1

    if DIO2_indicator:
        router1.set_dio_value(IOLine.DIO2_AD2, IOValue.HIGH)
        DIO2_indicator = not DIO2_indicator
    else:
        router1.set_dio_value(IOLine.DIO2_AD2, IOValue.LOW)
        DIO2_indicator = not DIO2_indicator


def read_values():

    global window
    global analog_reading
    global digital_reading
    global router1

    try:

        io_sample = router1.read_io_sample()

        digitalvalue = io_sample.get_digital_value(IOLine.DIO1_AD1)
        if digitalvalue == IOValue.LOW:
            digital_reading.set("Cerrado")
        elif digitalvalue == IOValue.HIGH:
            digital_reading.set("Abierto")

        analogvalue = io_sample.get_analog_value(IOLine.DIO0_AD0)
        analog_reading.set(analogvalue)

    except:
        pass

    window.after(500, read_values) # Programa la ejecucion de la funcion read_values para dentro de 500 milisegundos





l1 = Label(window, text="Serial Port:")
l1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Open Device", command=open_device)
b1.grid(row=0, column=2)

b2 = Button(window, text="Close Device", command=close_device)
b2.grid(row=0, column=3)

l2 = Label(window, text="Analogue Reading: ")
l2.grid(row=1, column=0)

analog_reading = DoubleVar()
l3 = Label(window, textvariable=analog_reading)
l3.grid(row=1, column=1)

b2 = Button(window, text="LED DIO2", command=led_status)
b2.grid(row=1, column=3)

l4 = Label(window, text="Digital Reading: ")
l4.grid(row=2, column=0)

digital_reading = StringVar()
l5 = Label(window, textvariable=digital_reading)
l5.grid(row=2, column=1)





window.mainloop() #Debe estar siempre al final del codigo
