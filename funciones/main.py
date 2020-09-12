'''
Una función es un
conjunto de instrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocando a
la funcion tantas veces como sea necesario.

def nombre_funcion(parametros):
  #codigo

nombre_funcion(mi_parametro)

#Ejemplo
print('Ejemplo uno')

def muestraNombres(nombre):
    print(f'El nombre es{nombre}')

muestraNombres('David')



def tabla(num):
    print(f'tabla de multiplicar {num}')
    for contador in range(11):
        print(f'La tabla del {num} * {contador}: {num*contador}')

num = int(input('Dame un numero: '))

tabla(num)
'''

'''
Parametros opcionales
def get_data(nombre, id=False):
    print(f'Hola señor {nombre} su ID es {id}')


get_data('david')
'''

'''
parametros opcionales y el return

'''

'''
def calculadora(numA, numB, basicas=False):
    suma = numA + numB
    resta = numA - numB
    multi = numA * numB
    divi = numA/numA

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multi: " + str(multi)
        cadena += "\n"
        cadena += "Divi: " + str(divi)

    return cadena

print(calculadora(5, 5, True))

'''

'''
fuenciones dentro de funciones
'''
'''
def getNombre(nombre):
    texto = f'El nombre es {nombre}'
    return texto

def getApellido(apellidos):
    texto = f'El apellidos es {apellidos}'
    return texto

def dameTodo(nombre, apellidos):
    texto = getNombre(nombre)+ "\n" + getApellido(apellidos)
    return texto

print(dameTodo("lodo", "lpz"))
'''

'''
Funciones lambda
es una funcion anonima
una funcion sin nombre
solo se usan para tareas simples y repetitivas
'''
'''
dime_el_year = lambda year: f'El año es {year}'

print(dime_el_year(2034))
'''