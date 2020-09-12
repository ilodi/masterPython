'''
Lista (arrays)
son colecciones o conjuntos de datos/valores,
bajo un unico nombre.
Para acceder a estos valores podemos usar un indice numerico
pelicula = "Batman"

# definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
# usando una tuppla
# una tupla es lo mismo que una lista pero
# esta no se puede modificar ejemplo list((valores))
cantantes = list(('billi', 'joel', 'mike'))

# lista mezclada
year = list(range(2020, 2050))
# lista vaidada
varia = ['lodo', 33, 4.4, True]
print(varia)
'''

# indices en listas

peliculas = ['GoT', 'Iron Man', 'Pokemon', 'Digimon']
'''
print(peliculas[1])
print(peliculas[-2])
print(peliculas[1:3])

#agregar elementos
peliculas.append("Yugioh")
peliculas.append("Zim")
print(peliculas)

# recorer una lista con for

print('¨¨¨¨¨¨¨¨¨Listado¨¨¨¨¨¨¨¨¨¨¨¨¨¨')

nueva_pelicula = ''
while nueva_pelicula != "parar":
    nueva_pelicula = input("Dame una nueva pelicula:")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f'{peliculas.index(pelicula)+1}.-Pelicula {pelicula}')


# lista multi dimensional
# listas dentro de listas
print('¨¨¨¨¨¨¨¨¨Listado contactos¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
contactos = [
    [
        'ema',
        'emaa@test.io'
    ],
    [
        'gema',
        'gema@test.io'
    ],
    [
        'lodo',
        'lodo@test.io'
    ]
]

print(contactos[1][1])

for contacto in contactos:
    for elmento in contacto:
        if contacto.index(elmento) == 0:
            print(f'nombre del usuario: {elmento}')
        else:
            print(f'email: {elmento}')
'''