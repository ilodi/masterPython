nombre = 'lodo'

# imprimir en panlla
print(nombre)
# saber el tipo de dato
print(type(nombre))
# detectar tipado
# el primer paramtro es lo que se evalua contra el 2 parametro
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esta variable es un string")
else:
    print("No es una cadena")
# comprueba directo
if not isinstance(nombre, float):
    print('La variable no es un numero con decimales')

# limpiar espacios
frase = "   Mi frase   Hola"
print(frase.strip())
# el punto es para acceder a un metodo

# eliminar variables
year = 2020
print(year)
del year
#print(f'ya no existe la variable {year}')

# comprobar si la variable esta vacia
texto = "Hola"

if len(texto) <= 0:
    print('El texto no tiene nada')
else:
    print('La variable tiene contenido:', len(texto))

# encontrar caracteres
frase = 'La vida es bella'
print(frase.find("vida"))

# remplazar palabras
# primer valor es el que va a buscar y el segundo el que va a cambiar
nueva_frase = frase.replace("vida", "caos")

print(nueva_frase)

# mayusculas
# minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())