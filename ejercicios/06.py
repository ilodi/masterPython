'''
todas las tables del 1 al 10
'''

for aux in range(1, 11):
    print('#########################')
    print(f'La tabla del {aux} es: ')
    print('#########################')
    for numero in range(1, 11):
        print(f'{aux} * {numero}: {aux*numero}')
