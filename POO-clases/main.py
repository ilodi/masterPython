# Programacion orientada a objetos (POO o OOP)

# definir una clase(molde para crear más objetos de ese tipo)
# (coche) con caracteristicas similares

class Coche:

    # atributos o propiedades(variables)
    # caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos, son acciones que hacen el objeto (coche) (funciones)
    # un metodo se define con una funcion
    # ayuda a acceder a las propiedades del ojeto
    # self es como decir yo mismo
    ###########################
    # metodo getter saca informacion
    # metodo setter agrega informacion

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        # returno sacar el valor del metodo
        return self.velocidad

# fin de definicion de clase


# Crear objeto / Instanciar la clase
coche = Coche()

print('Coche 1')
print(coche.marca)
print(f'Velocidad actual: {coche.getVelocidad()}')

# para acceder al metodo del objeto
for x in range(60):
    coche.acelerar()

coche.frenar()

print(f'Nueva velocidad: {coche.getVelocidad()}')

coche.setColor('verde')
coche.setModelo('Mursielago')
print(coche.marca, coche.getModelo(), coche.getColor())


print('---------------------------------------------')
# crear más objetos

coche2 = Coche()

coche2.setColor('amargo')
coche2.setColor('Gallardo')

print(coche2.getModelo() ,coche2.getColor())

print(type(coche2))