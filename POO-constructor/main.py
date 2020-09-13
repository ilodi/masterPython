# importar la clase
from coche import Coche

carro1 = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro2 = Coche("Verde", "Renault", "Megane", 150, 200, 4)
carro3 = Coche("Azul", "Renault", "Stepway", 150, 200, 4)
carro4 = Coche("plata", "Renault", "Duster", 150, 200, 4)


print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

#Detectar tipado
if type(carro3) == Coche:
    print('Es un objeto correcto')
else:
    print('No es de tipo Coche')

#Visibilidad
print(carro1.getPrivado())