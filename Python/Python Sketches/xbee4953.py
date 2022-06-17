import xbee

#NODOS#
vector_nodos = {'\x00\x13\xA2\x00\x40\xB0\x99\x5D':'nodo 1'}

#RESPUESTA#a
respuesta = '\x7E\x00\x17\x97\x01\x00\x13\xA2\x00\x40\xB0\x99\x5D\x0C\x61\x49\x53\x00\x01\x00\x0E\x01\x00\x04\x01\xBB\xF3'

nodo,digital_inputs,analog_inputs = xbee.respuesta4953(respuesta, vector_nodos)
print (nodo,digital_inputs, analog_inputs)

####
