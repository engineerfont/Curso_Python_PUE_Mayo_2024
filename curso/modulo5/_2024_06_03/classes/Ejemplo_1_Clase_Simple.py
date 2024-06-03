class Persona(object):
    nombre = 'xoan'
    __apellidos = 'gallego'

    def mostrar(self, msg, mayus = True):
        if mayus:
            print(msg.upper())
        else:
            print(msg)

persona = Persona()
persona.nombre='Luisa'
persona.mostrar('xoan')  # this
#print(persona.__apellidos)

persona2 = Persona()
persona2.nombre = 'Luis'

print(persona.nombre)
print(persona2.nombre)

persona3 = persona
print(persona3.nombre)

persona3.nombre = 'Margarita'
print(persona.nombre)
