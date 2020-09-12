'''
Es una estrutura de contorl que itera o repite la ejecicion de una 
serie de instrucciones tanatas veces comos ea necesario hasta que deje de cumplir

contador

While condicion:
  bloque
  actualizar el contador


contador = 1
muestrame = str(0)

while contador <= 1000:
  muestrame = muestrame + ", " + str(contador)
  contador += 1

print(muestrame)
'''

numero = int(input('Dame un numero si: '))

if numero < 1:
   numero = 1

print(f'tabla {numero}')

contador = 1
while contador <= 10:
  print(f'{contador} * {numero} = {contador*numero}')
  contador += 1

