'''
Programa que compruebe si una varibale esta vacia
y si es asi entonces que se rellene con 
texto en minusculas y mostrarlo en mayusculas
'''

x = ''

if not x:
    text = 'Hola mundo'
    x = text.lower()
    print(x)
else:
    print(f'El valor ya esta y es {x.upper()}')

print(x.upper())
'''
solucion
'''

text = ""
# borrar los espacios strip a los lados
if len(text.strip()) <= 0:
    # mostrar text
    text = "Soy un texto"
    print(text.upper())
else:
    print(f"La variable tiene contendio {text}")
