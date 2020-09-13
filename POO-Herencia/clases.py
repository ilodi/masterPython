# La herencia es la posibilidad de
# compartir atributos y métodos
# y  que diferentes clases hereden de otras

class Persona:
  # molde de classe padre
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return 'Estoy hablando'

    def caminar(self):
        return 'Estoy caminando'

    def dormir(self):
        return 'Estoy durmiendo'


#herredad de una clase padre
class Informatico(Persona):
    #constructor que dara valores al iniciar 
    def __init__(self):
        self.lenguajes = "HTML, CSS, JS"
        self.experiencia = 5

    def getLenguaje(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return 'Estoy programando'

    def reaparPC(self):
        return 'Estoy reparando'


class TecnicoRedes(Informatico):
    #para copiar un constructor del padre usas  super().__init__()
    def __init__(self):
        super().__init__()
        self.auditarRedes = 'Experto'
        self.experienciaRedes = 15
    

    def auditoria(self):
        return "Estoy auditando una red"

    