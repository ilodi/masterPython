'''
tiene un lista con 8 numeros
recorrela y mostrala
hacer una funcion que recora lista de numeros
ordenarla y mostrarla 
buscar un elemento que usuario pida por teclado
'''

# crear la lista
lista = [3, 5, 6, 2, 5, 6, 7, 2]


def mostrarLista(lista):
    resultado = ""
    for elmento in lista:
        resultado += str(elmento)
        resultado += "\n"
    return resultado


#recorer & mostrar
for numero in lista:
    print(numero)

#

try:
    print(mostrarLista(lista))

    busqueda = int(input('Que numero buscas?: '))

    #si es un numero?
    comprobar = isinstance(busqueda,int)

    while not comprobar or busqueda <=0:
        busqueda = int(input("Introduce el numero:"))
    else:
        print(f"Has introducido el numero {busqueda}")

    print(f"Buscar el num en {busqueda}")


    search= lista.index(busqueda)
    print(f"El numero {busqueda} Existe en la lista, es el indice {search}")
except:
    print('El número no esta en la lista')