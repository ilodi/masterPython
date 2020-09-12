# Capturar excepciones y manejar errores en codigo
# susceptible a fallos
# try va a intentar hacer algo
# except si try falla se ejecuta el except
# en otros lenguajes el except se llama catch
'''
try:
    nombre = input("cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usaurio = "El nombre es:"+nombre

    print(nombre_usaurio)
except:
    print("Ha ocuriod un error, mete bien el nombre")

# si todo sale bien y no hay error se puede poner un un else:

else:
    print('Todo funciona muy bien')

# finally detecta cuando se termina toda la iteracion de try,except, else

finally:
    print('Todo El ciclo termino sin problema alguno')
'''
'''
# manejar multiples errores
try:
    numero = int(input("Dime el unmero para elevarlo al cuadrado:"))
    print(f'El cuadrado del numero {numero} es {numero*numero}')
except TypeError:
    print("Debes convertir tus cadenas a enteros")
except ValueError:
    print("Introduce un número corecto")
except Exception as e:
    #saber los errores de una manera mas amigable
    print(type(e))
    print(f'Ha ocurrido un error: {type(e).__name__}')'''

# excepciones personalizadas o lanzar execpion

try:
    nombre = input('Introduce el nombre: ')
    edad = int(input('Indroduce la edad: '))

    if edad < 5 or edad > 110:
        # raise generas tu propio error
        raise ValueError('La edad introducida no es real')
    elif len(nombre) <= 1:
        raise ValueError('El nombres no es real')
    else:
        print(f'Bienvendio humano {nombre}')
except ValueError:
    print('Da los datos correctos')
except Exception as e:
    print(f'Existe un error : {e}')