class Persona(object):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def get_edad(self):
        return self.edad

    @get_edad.setter
    def get_edad(self, value):
        self.edad = value


persona = Persona('Encarna', 45)

'''print(persona.get_edad())
persona.set_edad(37)
print(persona.get_edad())'''

print(persona.get_edad)
persona.get_edad = 25
edades = 56 + persona.get_edad

