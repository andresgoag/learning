lonbyte = 2*2

def hexstr(h):
    h = format(h,'02X')
    if lonbyte-len(h)!= 0:
        h = ('0'*(lonbyte-len(h))) + h
    h = h.decode('hex')   
    return h









x = 65535
xh = hexstr(x)


d = ord(xh[0])*256+ord(xh[1])
print d





