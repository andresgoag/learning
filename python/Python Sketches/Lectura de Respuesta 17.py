def binario(decimal):
        binario = ''                                                                                                                                         
        while decimal//2 != 0:                                                                                                                               
            binario = str(decimal % 2) + binario                                                                                        
            decimal = decimal // 2                                                                                                                           
        return str(decimal) + binario                                                                                                                        
                                                                                                                                                             
def checksum(trama):
    suma = 0
    for i in trama:
        suma = suma+ord(i)
    h = hex(suma)
    h = h.split('x')[1]
    if len(h)%2 != 0:
        h = '0'+h
    h = h.decode('hex')
    checksum_dec = ord('\xFF')-ord(h[len(h)-1])
    checksum = hex(checksum_dec)
    checksum = checksum.split('x')[1]
    if len(checksum)%2 != 0:
        checksum = '0'+checksum 
    checksum = checksum.decode('hex')
    return checksum

def trama_17(res, vec_nod):                                                                                                                                                                                                                             ##
    byte = 0                            
    if res[byte] == '\x7E':                                                               
        byte = byte+1                                                                           
        lon_tra = ord(res[byte])*256+ord(res[byte+1])+1              
        if (lon_tra+3) == len(res):                                                
            byte = byte+2                                                                                                                                                                                                                                                                                                                                                  
            if res[byte] == '\x97' and res[byte+1] == '\x01':               
                tipo = 17                                                                       
            byte = byte+2                                                                                                                                                                                                                                                                                                 
            xbee = res[byte:byte+8]                                          
            for i in range(len(vec_nod)):               
                if xbee == vec_nod[i]:                                  
                    nodo = i                                                                    
            byte = byte+8                     
            byte = byte+2               
            if res[byte] == '\x49' and res[byte+1] == '\x53':
                comando = 4953                                                                  
            byte = byte+2                                                                                                                                                                               
            if res[byte] == '\x00':                               
                estado = 0                                                              
                byte = byte+1                                                           
                muestras = ord(res[byte])         
                byte = byte+1                                                                                                                                    
                dec_dig = ord(res[byte])*256+ord(res[byte+1])
                digital = byte                                         
                dig_in_mask = binario(dec_dig)                          
                cont = 0                                                                        
                dig_in = list()                                           
                for i in reversed(dig_in_mask):          
                    if i == '1':                                                
                        dig_in.append(cont)     
                    cont = cont+1                       
                byte = byte+2                           
                dec_analog = ord(res[byte])  
                analog = byte                                                        
                analog_in_mask = binario(dec_analog)
                cont = 0                                                                  
                analog_in = list()                                                  
                for i in reversed(analog_in_mask):                               
                    if i == '1':                                                              
                        analog_in.append(cont)                     
                    cont = cont+1                                                          
                byte = byte+1                                                                                                                                                                                                           
                if res[digital] != '\x00' or res[digital+1] != '\x00':
                    dec3 = ord(res[byte])*256+ord(res[byte+1])  
                    dec3 = dec3|8192
                    dig_read_mask = binario(dec3)
                    count = 0                                                                   
                    index = 0                                                                   
                    for i in reversed(dig_read_mask):                                  
                        if count < 13:  
                            if index < len(dig_in) and count == dig_in[index]:
                                if i == '0':                                            
                                    dig_in[index] = [dig_in[index],0]
                                    index = index+1                                             
                                else:                                                           
                                    dig_in[index] = [dig_in[index],1]           
                                    index = index+1                                            
                        count = count+1                                                         
                    byte = byte+2
                if res[analog] != '0':  
                    for i in range(len(analog_in)):                                       
                        analog_read = ord(res[byte])*256+ord(res[byte+1])
                        v = (float(analog_read)/1023.0)*1200
                        analog_in[i] = [analog_in[i],v]                                 
                        byte = byte+2


                cksm = checksum(res[3:-1])
                if res[byte] == cksm:
                    return  nodo,dig_in,analog_in            #POSIBLES RESULTADOS: lon_tra,tipo,comando,estado,muestras,
                else:
                    return -1,-1,-1
                    print 'Checksum erroneo'
            else:                        
                return -1,-1,-1                                                    
                print 'El comando no se recibio bien'

               
                                                                                                                                                           
#NODOS#
nodo1 = '\x00\x13\xA2\x00\x40\xC1\x2A\x03'
nodo2 = '\x00\x13\xA2\x00\x40\x33\x1C\xF9'
nodo3 = '\x00\x13\xA2\x00\x42\x33\x1C\xF9'
vector_nodos = [nodo1, nodo2, nodo3]

#RESPUESTA#
respuesta = '\x7E\x00\x19\x97\x01\x00\x13\xA2\x00\x40\xC1\x2A\x03\x79\x5B\x49\x53\x00\x01\x00\x1C\x03\x00\x04\x02\x12\x02\x1B\xBF'

nodo,dig_in,analog_in = trama_17(respuesta, vector_nodos)
print nodo,dig_in, analog_in
