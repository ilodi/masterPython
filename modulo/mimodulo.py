#crear modulo
def holaMundo(nombre):
    return f'Hola como estas, {nombre}'


def calculadora(numA, numB, basicas=False):
    suma = numA + numB
    resta = numA - numB
    multi = numA * numB
    divi = numA/numA

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multi: " + str(multi)
        cadena += "\n"
        cadena += "Divi: " + str(divi)

    return cadena
