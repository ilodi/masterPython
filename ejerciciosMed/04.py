'''
1.- crea 4 variables (una, lista, un string, un entero y un boleano)
2.- comprobar el tipo de dato y lo imprima
'''

'''
def que_tipo_es(dato, tipo):
    return print(f'El valor dado es del tipo {type(x)}')
'''
def comprobarTipado(dato, tipo):
    #retornara un true si es verdad
    test = isinstance(dato, tipo)
    result = ""
    if test:
        result = f'Este dato es del tipo {type(dato)}'
    else:
        result=None
    return result

lista = ['charmander', 'pikachu', 'mew']
text = "Tengo que ser siempre el mejor"
numero = 150
existen = True

print(comprobarTipado(lista, list))

#print(que_tipo_es(numero))