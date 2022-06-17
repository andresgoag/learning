datos = open('aga.txt','w')
datos.close()

def escribir(x):
    datos = open('aga.txt','a')
    datos.write(x)
    datos.write('\n')
    datos.close()
    


while True:
    x = raw_input(':')
    escribir(x)

