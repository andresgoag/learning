
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.io import IOLine, IOMode, IOValue, IOSample
import time



PORT = "COM4"
BAUD_RATE = 9600
REMOTE_NODE_ID = "Router1"
ANALOG_LINE = IOLine.DIO0_AD0
DIGITAL_LINE = IOLine.DIO1_AD1
IOLINE_OUT = IOLine.DIO2_AD2



device = XBeeDevice(PORT, BAUD_RATE)


try:
    device.open()



    # Obtain the remote XBee device from the XBee network.
    xbee_network = device.get_network()
    remote_device = xbee_network.discover_device(REMOTE_NODE_ID)

    if remote_device is None:
        print("Could not find the remote device")
        exit(1)



    #remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041046C30"))





    # Set the local device as destination address of the remote.
    remote_device.set_dest_address(device.get_64bit_addr())
    remote_device.set_io_configuration(ANALOG_LINE, IOMode.ADC)
    remote_device.set_io_configuration(DIGITAL_LINE, IOMode.DIGITAL_IN)
    remote_device.set_io_configuration(IOLINE_OUT, IOMode.DIGITAL_OUT_LOW)



    x = True

    while True:
        io_sample = remote_device.read_io_sample()


        sensor_puerta = IOLine.DIO1_AD1
        digitalvalue = io_sample.get_digital_value(sensor_puerta)
        if digitalvalue == IOValue.LOW:
            print("La entrada esta en bajo")

        potenciometro = IOLine.DIO0_AD0
        analogvalue = io_sample.get_analog_value(potenciometro)
        print(analogvalue)


        if x:
            remote_device.set_dio_value(IOLINE_OUT, IOValue.LOW)
            x = not x
        else:
            remote_device.set_dio_value(IOLINE_OUT, IOValue.HIGH)
            x = not x

        time.sleep(0.5)





finally:
    if device is not None and device.is_open():
        device.close()
