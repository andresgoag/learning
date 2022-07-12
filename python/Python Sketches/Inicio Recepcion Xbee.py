exit = 0
while exit == 0:
    ini = ser.read()
    if ini == '\x7E':
        lon = ser.read(2)
        dec_lon = ord(lon[0])*256+ord(lon[1])+1
        res = ser.read(dec_lon)
        res = ini+lon+res
        exit = 1
