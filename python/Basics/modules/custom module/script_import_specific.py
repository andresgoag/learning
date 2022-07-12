#El archivo de python del modulo xbee debe estar ubicado en la carpeta donde se ejecuta el script o en la carpeta site-packages de la instalacion de python.

from xbee import XBeeDevice as xbeedev, ZigBeeDevice


x = [1,2,3,4,5]



print(dir(xbeedev))
suma = xbeedev.checksum(x)
print(suma)



print(dir(ZigBeeDevice))
suma = ZigBeeDevice.crs(x)
print(suma)
