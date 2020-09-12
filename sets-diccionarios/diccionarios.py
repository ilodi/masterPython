'''
Un diccionario es como una lista
pero el indixe no es numerico
es como un json
'''
'''
persona = {
    "nombre": "David",
    "apellidos": "lpz",
    "web": "lodo.mx"
}

print(type(persona))
print(persona)

print(persona["web"])
'''

# lista con Diccionario
contactos = [
    {
        'nombre': 'David',
        'email': 'david@gm.cm'
    },
    {
        'nombre': 'Eduardo',
        'email': 'edu@gm.cm'
    },
    {
        'nombre': 'max',
        'max': 'david@gm.cm'
    }
]


print(contactos[1]['nombre'])

for contacto in contactos:
    print(f"Nombre de los contactos: {contacto['nombre']}")
