#Referencias: https://www.hackster.io/ahmedibrrahim/smart-home-automation-iot-using-raspberry-pi-and-python-47fb62
#Referencias: https://github.com/soumilshah1995/Flask-Charts-Youtube-Tutorials-

from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.io import IOLine, IOMode, IOValue, IOSample
from flask import Flask, render_template, request


app = Flask(__name__)


remote_device = None




@app.before_first_request #Esta funcion correra una unica vez antes del primer request
def before_first_request_func():
    global remote_device
    device = XBeeDevice("COM4", 9600)
    remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041046C30"))
    device.open()
    remote_device.set_io_configuration(IOLine.DIO2_AD2, IOMode.DIGITAL_OUT_LOW)
    remote_device.set_io_configuration(IOLine.DIO1_AD1, IOMode.DIGITAL_IN)
    remote_device.set_io_configuration(IOLine.DIO0_AD0, IOMode.ADC)




@app.route('/')
def index():
    templateData = {'ledRed' : "Inicializando", 'sensorpuerta':"Inicializando"}
    return render_template('index.html', **templateData)




@app.route('/<deviceName>/<action>')
def do(deviceName, action):
    global remote_device

    if action == "on":
        remote_device.set_dio_value(IOLine.DIO2_AD2, IOValue.HIGH)
        valor = "prendido"

    if action == "off":
        remote_device.set_dio_value(IOLine.DIO2_AD2, IOValue.LOW)
        valor = "apagado"

    templateData = {'ledRed' : valor}
    return render_template('index.html', **templateData )





@app.route('/data', methods=["GET", "POST"])
def data():

    io_sample = remote_device.read_io_sample()
    analogread = io_sample.get_analog_value(IOLine.DIO0_AD0)

    digitalvalue = io_sample.get_digital_value(IOLine.DIO1_AD1)
    if digitalvalue == IOValue.LOW:
        dio = "Cerrado"
    if digitalvalue == IOValue.HIGH:
        dio = "Abierto"

    data = {"analogread":analogread, "digitalread":dio} #diccionario para formatear como json la lista de valores creada.
    return data






if __name__ == "__main__":
    app.run(debug=True)
