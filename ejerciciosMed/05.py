'''
Ejercicio crea una lista con el contenido de esta tabla
ACCION AVENTURA         DEPORTES
gta      assins         FIFA
cod       crash          Pro
pubb    prince of        MotoGp

mOSTRAR ESTA TABLA ORDENADA
'''

tabla = [
    {
        "categoria": "ACCIÓN",
        "juegos": [
            'GTA', 'COD', 'PUGB'
        ]
    },
       {
        "categoria": "AVENTURA",
        "juegos": [
            'ASSINS', 'CRASH', 'Prince of persia'
        ]
    },
       {
        "categoria": "DEPORTES",
        "juegos": [
            'FIFA 21', 'PRO 21', 'MOTO GP 21'
        ]
    }
]

for categoria in tabla: 
    print(f"Categoria {categoria['categoria']}")
    for juego in categoria['juegos']:
        print(f"Los Juegos {juego}")