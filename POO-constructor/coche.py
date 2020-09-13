class Coche:
    # atributos o propiedades(variables)
    # caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    soy_publico = 'Hola, soy un atributo publico'
    #__ es para decir que es una propiedad privada
    __soy_privado = 'Soy un atributo privado'

    #acceder aun metodo privado
    def getPrivado(self):
        return self.__soy_privado

    # El construcctor es el primer metodo que se ejecuta en la clases
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

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

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        # returno sacar el valor del metodo
        return self.velocidad
    
    def getInfo(self):
        info = "------ Informaciòn del coche ---"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info
