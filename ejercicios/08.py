'''
Sacar el porcentaje del numero que quiere el usaurio
'''

numero = int(input('Dame un numero: '))
porcentaje = int(input('El porcentaje: '))

if numero > 0:
  respuesta = (porcentaje/100)*numero
  print(respuesta)
else:
  print(f'algo no esta bien')