#El archivo de python del modulo xbee debe estar ubicado en la carpeta donde se ejecuta el script o en la carpeta site-packages de la instalacion de python.

import xbee


x = [1,2,3,4,5]



print(dir(xbee.XBeeDevice))
suma = xbee.XBeeDevice.checksum(x)
print(suma)



print(dir(xbee.ZigBeeDevice))
suma = xbee.ZigBeeDevice.crs(x)
print(suma)
