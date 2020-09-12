'''
Un paquete es un conjunto de modulos, herramientas
'''
'''
el __pychache__ no se debe de tocar
'''
print("PROBANDO PAQUETES:")

#importat paquete
from mipaquete import pruebas
from mipaquete import herramientas
#importat todo
from mipaquete import pruebas,herramientas

pruebas.probando()
herramientas.combreCompleto('Lodo', 'lpz')