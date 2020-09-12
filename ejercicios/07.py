'''
numero impares entre dos numeros que de el usuari

'''

x = int(input('Numero A: '))
y = int(input('Numero B: '))

if x < y:
  for contador in range (x, (y+1)):
    if contador%2 != 0:
      print(f'Estos son los numeros impares {contador}')
else:
  print(f'Los valores no son validos')