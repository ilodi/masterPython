'''
Modulos: funcionalidades ya hechas para reutilizar
un modulo es como una libreria.
'''
#importar modulo
###import mimodulo
#importat una sola funcion de un modulo
###from mimodulo import holaMundo
#importar todas las funciones
###from mimodulo import *
'''
print(holaMundo('Lodo'))

print(calculadora(3,4,False))
'''

#modulo fechas
import datetime
'''
print(datetime.date.today())
fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S ")

print(fecha_personalizada)

print(datetime.datetime.now().timestamp())
'''
#Modulo matematicas
import math
print("Raiz cuadrada de 10:", math.sqrt(10))
print(f"Numero de pi: {float(math.pi)}")
print(f"Redondear arriba {math.ceil(0.333333)}")
print(f"Redondear abajo {math.floor(0.333333)}")

#modulo random
import random

print('Numero aleatorio 15 a 67', random.randint(15,67) )