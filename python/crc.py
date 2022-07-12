import libscrc

a = '0103020030'
query = bytes.fromhex(a)
crc = libscrc.modbus(query)
crc16 = crc.to_bytes(2, byteorder='little')
print(crc16.hex())