'''

'''
# ejemplo I
'''
print("############## EJEMPLO I ##############")

color = input("Adivina el color:")

if color == "rojo":
  print("El color es rojo")
else:
  print("color no es rojo")
  '''

'''
print("############## EJEMPLO IF anidado ##############")

nombre = input("Cual es tu nombre: ")
ciudad = input("Ciudad: ")
pais = input("Cual es tu pais: ")
edad = int(input("Que edad tienes: "))
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if pais != "mexico":
        print("El no eres mexicano")
        if edad >= 21:
          print("Eres mayor de edad en USA")
    else:
        print(f"Eres Méxicano y vives en {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")


print("############## EJEMPLO elsif anidado ##############")

dia = int(input("Que dia es hoy:"))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 4:
    print("Es martes")
else:
    print("no es un dia")
'''

'''
if x >= y and x<=z
if x >= y or x<=z
if x >= y !=
 x<=z
if x >= y not x<=z

if not (codicion)
'''