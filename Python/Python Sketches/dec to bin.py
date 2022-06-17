x = 156


def binario(decimal):                                                                                                                                        ##
        binario = ''                                                                                                                                         ##
        while decimal//2 != 0:                                                                                                                               ##
            binario = str(decimal % 2) + binario                                                                                                             ##
            decimal = decimal // 2                                                                                                                           ##
        return str(decimal) + binario


s = binario(x)

print s
