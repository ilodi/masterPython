# importar todo el archivo
import clases

persona = clases.Persona()
persona.setNombre('Lodi')
persona.setApellidos('lpz')
persona.setAltura("178cm")
persona.setEdad('28')

print(f'La persona es: {persona.getNombre()} {persona.getApellidos()}')
print(persona.hablar())
print('----------------------------')
informatico = clases.Informatico()
informatico.setNombre('David')
informatico.setApellidos('Lopez')
informatico.setAltura('150 cm')

print(
    f'La informatico es: {informatico.getNombre()} {informatico.getApellidos()}')
print(informatico.programar())

print('--------------------')

tecnico = clases.TecnicoRedes()

print(tecnico.auditoria(), tecnico.getLenguaje())
