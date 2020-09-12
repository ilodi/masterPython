'''
Todos los numero entre dos numeros que te den
'''

x = int(input('Dame el primer numero: '))
y = int(input('Dame el segundo numero: '))


if ( x < y):
  for aux in range(x, (y+1)):
    print(aux)
else: 
  print('El numero un debe de ser menos al numero dos')