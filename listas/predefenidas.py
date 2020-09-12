'''
'''
cantantes = ['billie', 'mike', 'tree', 'dio']
numeros = [1, 2, 3, 4, 5, 3, 4]

# ordenar una lista
print(numeros)
numeros.sort()
print(numeros)

# agregar elmentos a una lista son igual a los arrays
# lo agrega al final
cantantes.append('clear')
# lo agrega en orden
cantantes.insert(1, "Toña ")
print(cantantes)

# eliminar elements
cantantes.pop(1)
# elimar directo
cantantes.remove('tree')
print(cantantes)


# dar la vuelta
numeros.reverse()
print(numeros)

# encontrar el numero de elementos
print('mike' in cantantes)
print('aquii')
# contar elementos
print(len(cantantes))

#cuantas veces aparece un elemento en la 
numeros.append(3)
print(numeros.count(3))

#conseguir indice
print(cantantes.index("mike"))

#unir listas
cantantes.extend(numeros)
print(cantantes)