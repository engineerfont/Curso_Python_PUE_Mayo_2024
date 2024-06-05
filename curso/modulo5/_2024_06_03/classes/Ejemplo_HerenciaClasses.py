class Persona(object):

    def __init__(self, nombre='', edad=0):
        self.nombre = nombre
        self.edad = edad
        self.__fecha = '2023-11-29'

    def datos(self):
        return f'Nombre = {self.nombre}, Edad = {self.edad}'

class Usuario(Persona):

    # El parámetro 'persona' representa un objeto de tipo 'Persona'
    def __init__(self, persona):

        #super().__init__(nombre, edad)
        Persona.__init__(self, persona.nombre, persona.edad)


    def ver_datos(self):
        data = super().datos()
        #print(data)
        #print(self.__fecha)
        return f'Nombre = {self.nombre.upper()}, Edad = {self.edad}'


'''u = Usuario('Xoan', 43)
print(u.ver_datos())
print(u.datos())

print(u.nombre)
print(u.__fecha)'''


persona = Persona('Mía', 4)
#persona2 = persona
user = Usuario(persona)

print(user.ver_datos())

