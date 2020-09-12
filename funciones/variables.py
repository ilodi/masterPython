'''
las variables globales estan disponibles en todas partes
'''

#global
frase = "Los gatos son genios"

print(frase)

def holaMundo():
    frase ="Hola mundillo"
    print('dentro del def')
    print(frase)
    #hacer global
    global year
    year = 2021
    print(year)

holaMundo()

