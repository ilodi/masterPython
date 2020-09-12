'''
Escribe un program que agregue valores a una lista mientras sea menor a 120 la longitud
Plus: usae While y for
'''

coleccion = []

contador = 1
while contador < 120:
    valor = int(input('Dame un valor para la lista: '))
    print(f"Haz agregado el valor {valor}")
    print(f"Coleccion tiene {len(coleccion)}")
    coleccion.append(valor)
    print(f"Coleccion tiene ahora {len(coleccion)}")
    contador += 1
else:
    print('Ya cuenta con los valores maximos')
'''
for contador in range(0,120):
    coleccion.append(f"elemto-{contador}")
    print(f"Mostando el: {coleccion[contador]}")
else:
    print(coleccion)
'''