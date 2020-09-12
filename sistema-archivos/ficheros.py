import os.path
import os
from io import open
# obtener ruta absoluta
import pathlib
# funciones extras
import shutil

# abrir archivo
#ruta , permisos
ruta = str(pathlib.Path().absolute())+"/fichero_text.txt"
archivo = open(ruta, "a+")

# escribir a un archivo
archivo.write("Hola mundo soy un texto\n")

# cerrar archivo
archivo.close()

# Abrir arichivo

ruta = str(pathlib.Path().absolute())+"/fichero_text.txt"
archivo_lectura = open(ruta, "r")
# leer contenido
'''
contenido = archivo_lectura.read()
print(contenido)
'''
# leer contenido y guardarlo en lista

lista = archivo_lectura.readlines()
archivo_lectura.close()

for elemento in lista:
  #  if not elemento.isnumeric():
  # split una frace es una lista
    lista_frase = elemento.split()
    print(f"--{lista_frase}")
    print(f"--{elemento.upper()}")

# copiar un archivo
'''
ruta_original = str(pathlib.Path().absolute())+"/fichero_text.txt"
ruta_nueva = str(pathlib.Path().absolute())+"/copia_fichero.txt"


shutil.copyfile(ruta_original, ruta_nueva)
'''
# mover archivo
'''
ruta_original = str(pathlib.Path().absolute())+"/fichero_copia.txt"
ruta_copil = str(pathlib.Path().absolute())+"/fichero_copia_A.txt"

shutil.move(ruta_original,ruta_copil)
'''
# elimiar archivo
ruta_original = str(pathlib.Path().absolute())+"/fichero_text.txt"
os.remove(ruta_original)

# como saber si el archivo exite

# ruta absoluta direcctoria actual
# print(os.path.abspath("./"))

if os.path.isfile(os.path.abspath("./")+"/fichero_text.txt"):
    print('El archivo esta')
else:
    print('El archivo no esta')
