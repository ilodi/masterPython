'''
for variable in elemento_iterable(list, rango, etc)
range(crea numero de x a y)

contador = 0
resultado = 0

for contador in range(0,90):
  print(contador)
 # resultado = resultado+contador
  resultado += contador

print(f':::{resultado}')

'''

numero = int(input('De quien quieres hacer la tabla de multiplicar: '))

if numero <= 1:
    numero = 1
print(f'Tabla de multiplicar del numero {numero}')

for numero_tabla in range(0, 11):
  print(f'{numero} * {numero_tabla} = {numero_tabla*numero}')
  #cortar el bucle con break
else:
  ("Tabla finalizada.")