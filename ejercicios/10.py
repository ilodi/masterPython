'''
nota de 15 alumnos
'''

contador = 1
aprobados = 0
supendidos = 0
numero_alumnos = int(input('Cunatos alumnos tienes: '))

while contador <= numero_alumnos:
    nota = int(input(f'Que nota quieres al almno {contador}: '))
    if nota >= 5:
        aprobados += 1
    else:
        supendidos += 1
    contador += 1

print(f'Alumnos aprobados: {aprobados}')
print(f'Alumnos suspendidos: {supendidos}')
