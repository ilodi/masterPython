'''
los cuadrados de los 60 primero numero .
con los dos bucles
'''

#while

contador = 1

while contador <= 60:
  print(f'El cuadrado de {contador} es: {contador*contador}')
  contador += 1

print("Por FOR")

for contador in range(1, 61):
    print(f'El cuadrado de {contador} es: {contador*contador}')
