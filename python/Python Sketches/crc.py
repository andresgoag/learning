res = '\x01\x01\x01\x10'


def crc_1(respuesta):
    crc = ord('\xFF')*256 + ord('\xFF')
    for i in range(len(respuesta)):
        crc = crc^ord(respuesta[i])
        for j in range(8):
            if crc%2 == 0:
                crc = crc/2
            else:
                crc = crc/2
                crc = crc^(ord('\xA0')*256+ord('\x01'))
    crc = hex(crc)
    crc = crc.split('x')[1]
    if len(crc)%2 != 0:
        crc = '0'+crc
    crc = crc.decode('hex')
    return crc



crc = crc_1(res)
print crc.encode('hex')
