##################################################FUNCION PARA LEER TRAMAS DE RESPUESTA DE ESTADO DE PUERTOS###################################################
#CONVERTIR A BINARIO#                                                                                                                                        ##
def binario(decimal):                                                                                                                                        ##
        binario = ''                                                                                                                                         ##
        while decimal//2 != 0:                                                                                                                               ##
            binario = str(decimal % 2) + binario                                                                                                             ##
            decimal = decimal // 2                                                                                                                           ##
        return str(decimal) + binario                                                                                                                        ##
                                                                                                                                                             ##
                                                                                                                                                             ##
def trama(respuesta, vector_nodos):                                                                                                                          ##
                                                                                                                                                             ##
    byte = 0                                                                                    #INICIA EL CONTADOR DE BYTES                                 ##
    if respuesta[byte] == '\x7E':                                                               #VERIFICA EL INICIO DE TRAMA                                 ##
        byte = byte+1                                                                           #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##                   
                                                                                                                                                             ##
        longitud_trama = ord(respuesta[byte])*256+ord(respuesta[byte+1])+1                      #CALCULA LA LONGITUD DE LA TRAMA DESDE EL 4 BYTE             ##
        if (longitud_trama+3) == len(respuesta):                                                #VERIFICA LA LONGITUD CALCULADA CON LA REAL                  ##
            byte = byte+2                                                                       #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##
                                                                                                                                                             ##
            if respuesta[byte] == '\x97' and respuesta[byte+1] == '\x01':                       #IDENTIFICA EL TIPO DE TRAMA AL QUE RESPONDE...              ##
                tipo = 17                                                                       #IDENTIFICADOR DE TIPO DE RESPUESTA                          ##
            byte = byte+2                                                                       #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##
                                                                                                                                                             ##
            xbee_respondiendo = respuesta[byte:byte+8]                                          #IDENTIFICA LA DIRECCION DEL NODO QUE RESPONDE               ##
            for i in range(len(vector_nodos)):                                                  #ITERA EN EL VECTOR DE NODOS                                 ##
                if xbee_respondiendo == vector_nodos[i]:                                        #COMPARA LA DIRECCION QUE RESPONDIO CON LOS NODOS            ##
                    nodo = i                                                                    #IDENTIFICADOR DEL NODO QUE RESPONDE                         ##
            byte = byte+8                                                                       #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##
                                                                                                                                                             ##
            byte = byte+2                                                                       #DIRECCION DE 16 BITS                                        ##
                                                                                                                                                             ##
                                                                                                                                                             ##
            if respuesta[byte] == '\x49' and respuesta[byte+1] == '\x53':                       #IDENTIFICA COMANDO AL QUE RESPONDE...                       ##
                comando = 4953                                                                  #IDENTIFICADOR                                               ##
            byte = byte+2                                                                       #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##
                                                                                                                                                             ##
            if respuesta[byte] == '\x00':                                                       #IDENTIFICACION ESTADO DEL COMANDO                           ##
                estado = 0                                                                      #ESTADO DEL COMANDO                                          ##
                byte = byte+1                                                                   #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##
                                                                                                                                                             ##
                muestras = ord(respuesta[byte])                                                 #NUMERO DE SAMPLES RECIBIDOS                                 ##
                byte = byte+1                                                                   #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##
                                                                                                                                                             ##
                decimal_digital = ord(respuesta[byte])*256+ord(respuesta[byte+1])               #LEE LA INFORMACION DE ENTRADAS DIGITALES HABILITADAS        ##
                digital = byte                                                                  #BYTE QUE TRAE EL DIGITAL INPUT MASK                         ##
                digital_input_mask = binario(decimal_digital)                                   #CREA EL DIGITAL INPUT MASK                                  ##
                cont = 0                                                                        #INICIA EL CONTADOR                                          ##
                digital_inputs = list()                                                         #CREA UNA LISTA VACIA PARA ALMACENAR LAS LECTURAS DIGITALES  ##
                for i in reversed(digital_input_mask):                                          #ITERA EN EL DIGITAL INPUT MASK                              ##
                    if i == '1':                                                                #SI ESTA HABILITADO COMO DIO...                              ##
                        digital_inputs.append(cont)                                             #SE ADICIONA LA ENTRADA DIO A digital_inputs                 ##
                    cont = cont+1                                                               #CONTADOR                                                    ##
                byte = byte+2                                                                   #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##
                                                                                                                                                             ##
                decimal_analogo = ord(respuesta[byte])                                          #LEE LA INFORMACION DE ENTRADAS ANALOGAS HABILITADAS         ##
                analog = byte                                                                   #BYTE QUE TRAE EL ANALOG INPUT MASK                          ##
                analog_input_mask = binario(decimal_analogo)                                    #CREA EL ANALOG INPUT MASK                                   ##
                cont = 0                                                                        #INICIA EL CONTADOR                                          ##
                analog_inputs = list()                                                          #CREA UNA LISTA VACIA PARA ALMACENAR LAS LECTURAS ANALOGAS   ##
                for i in reversed(analog_input_mask):                                           #ITERA EN EL ANALOG INPUT MASK                               ##
                    if i == '1':                                                                #SI ESTA HABILITADO COMO ANALOG INPUT...                     ##
                        analog_inputs.append(cont)                                              #SE ADICIONA EL ANALOG INPUT A analog_inputs                 ##
                    cont = cont+1                                                               #CONTADOR                                                    ##
                byte = byte+1                                                                   #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##
                                                                                                                                                             ##
                if respuesta[digital] != '\x00' or respuesta[digital+1] != '\x00':              #SI EL DIGITAL INPUT MASK ES DIFERENTE DE 0...               ##
                    decimal3 = ord(respuesta[byte])*256+ord(respuesta[byte+1])                  #LEE LA INFORMACION DE ESTADO DE DIGITALES                   ##
                    decimal3 = decimal3|8192                                                    #   -----                                                    ##
                    digital_reading_mask = binario(decimal3)                                    #CREA EL DIGITAL READING MASK                                ##
                    count = 0                                                                   #INICIA EL CONTADOR                                          ##
                    index = 0                                                                   #INICIA EL INDEX                                             ##
                    for i in reversed(digital_reading_mask):                                    #ITERA EN EL DIGITAL READING MASK                            ##
                        if count < 13:                                                          #SE ASEGURA DE LEER LAS 13 POSIBLES DIO                      ##
                            if index < len(digital_inputs) and count == digital_inputs[index]:  #VERIFICA QUE NO SE OCURRA UN INDEX OUT OF RANGE             ##
                                if i == '0':                                                    #SI LA LECTURA ES 0...                                       ##
                                    digital_inputs[index] = [digital_inputs[index],0]           #LA ENTRADA ESTA EN BAJO, SE ADICIONA AL VECTOR DIGITAL      ##
                                    index = index+1                                             #SIGUIENTE LECTURA                                           ##
                                else:                                                           #SI LA LECTURA ES 0...                                       ##
                                    digital_inputs[index] = [digital_inputs[index],1]           #LA ENTRADA ESTA EN ALTO, SE ADICIONA AL VECTOR DIGITAL      ##
                                    index = index+1                                             #SIGUIENTE LECTURA                                           ##
                        count = count+1                                                         #SIGUIENTE LECTURA                                           ##
                    byte = byte+2                                                               #PASA AL SIGUIENTE SEGMENTO DE TRAMA                         ##
                                                                                                                                                             ##
                                                                                                                                                             ##
                if respuesta[analog] != '0':                                                    #SI EL ANALOG INPUT MASK ES DIFERENTE DE 0...                ##
                    for i in range(len(analog_inputs)):                                         #SE ITERA EN EL ANALOG INPUTS                                ##
                        analog_reading = ord(respuesta[byte])*256+ord(respuesta[byte+1])        #INTERPRETA LA LECTURA                                       ##
                        v = (float(analog_reading)/1023.0)*1200                                 #CONVIERTE LA LECTURA EN MILIVOLTIOS                         ##
                        analog_inputs[i] = [analog_inputs[i],v]                                 #SE ADICIONA LA LECTURA A SU RESPECTIVO AD0                  ##
                        byte = byte+2                                                           #PASA A LA SIGUIENTE LECTURA                                 ##
                                                                                                                                                             ##
                                                                                                                                                             ##
                return digital_inputs,analog_inputs                                             #DEVUELVE LOS RESULTADOS                                     ##
                #return longitud_trama,tipo,nodo,comando,estado,muestras,digital_inputs,analog_inputs POSIBLES RESULTADOS                                    ##                                                                                                                                       #
                                                                                                                                                             ##
            else:                                                                               #SI EL COMANDO NO SE RECIBIO BIEN...                         ##                   
                return list(), list()                                                           #DEVUELVE TODO VACIO                                         ##
                print 'El comando no se recibio bien'                                                                                                        ##
        else:                                                                                   #SI LA LONGITUD DE TRAMA NO COINCIDE CON LA RESPUESTA...     ##
            return list(), list()                                                               #DEVUELVE TODO VACIO                                         ##
            print 'Error de coincidencia en la longitud de trama'                                                                                            ##
    else:                                                                                       #SI EL INICIO DE TRAMA ES ERRONEO...                         ##
        return list(), list()                                                                   #DEVUELVE TODO VACIO                                         ##
        print 'Inicio de trama erroneo'                                                                                                                      ##
                                                                                                                                                             ##
##################################################FUNCION PARA LEER TRAMAS DE RESPUESTA DE ESTADO DE PUERTOS###################################################
#NODOS#
nodo1 = '\x00\x13\xA2\x00\x40\xC1\x2A\x03'
nodo2 = '\x00\x13\xA2\x00\x40\x33\x1C\xF9'
nodo3 = '\x00\x13\xA2\x00\x42\x33\x1C\xF9'
vector_nodos = [nodo1, nodo2, nodo3]

#RESPUESTA#
respuesta = '\x7E\x00\x19\x97\x01\x00\x13\xA2\x00\x40\xC1\x2A\x03\x79\x5B\x49\x53\x00\x01\x00\x1C\x03\x00\x04\x02\x12\x02\x1B\xBF'

digital_inputs,analog_inputs = trama(respuesta, vector_nodos)
print digital_inputs, analog_inputs
