import serial
import time
ser = serial.Serial('COM6', 9600, timeout=1)

if ser.is_open:
    ser.close()

ser.open()

router = '\x00\x13\xA2\x00\x40\xA8\x42\x9A'


while True:

    try:
        byte = ser.read()
        if byte == '\x7E':
            start_delimiter = byte
            
            length_hex = ser.read(2)
            
            byte = ser.read()
            if byte == '\x92':
                frame_type = byte

                address64 = ser.read(8)
                if address64 == router:
                    address16 = ser.read(2)
                    
                    byte = ser.read()
                    if byte == '\x01':
                        receive_option = byte

                        byte = ser.read()
                        if byte == '\x01':
                            n_samples = byte

                            digital = ser.read(2)
                            analog = ser.read()
                            info = ser.read(2)
                            check = ser.read()

                            trama = start_delimiter+length_hex+frame_type+address64+address16+receive_option+n_samples+digital+analog+info+check
                            print trama.encode('hex')
                            

                    
                    
        
         

    except:
        print 'nada en el puerto'
    time.sleep(0.001)

ser.close()

