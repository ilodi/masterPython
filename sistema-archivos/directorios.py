import os, shutil

#crear carpeta

#verifica si la carpeta existe
if not os.path.isdir('./mi_carpeta'):
    os.mkdir('./mi_carpeta')
else:
    print('Ya existe el directorio')

#elimianr
#os.rmdir('./mi_carpeta')
'''
#copiar carpeta
ruta_original = './mi_carpeta'
ruta_nueva = './mi_carpeta_copiada'

shutil.copytree(ruta_original, ruta_nueva)

#elimianr
os.rmdir('./mi_carpeta_copiada')
'''

#poder listar los archivos

print(f'contenido :')
contenidoA = os.listdir('./mi_carpeta')
print(contenidoA)

for carpeta in contenidoA:
    print(carpeta)